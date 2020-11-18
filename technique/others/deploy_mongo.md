MongoDB部署文档
背景
目前平台使用mysql中存储了大量的json数据，这些json数据存在下面一些问题：
- 数据不方便检索，一些json数据字段嵌套已经非常严重
- 数据更新容易出错，比如策略合约或策略的一些属性数据更新，容易导致实盘问题
- 一些相同的json数据重复放在不同的字段中

同时单一的关系型数据在使用过程中也存在一些问题：
- 业务初期定义强关系型表结构比较困难
- 业务变化时，更改表结构困难，导致后台代码被迫适应去适应表结构
- 技术代码改进困难，重构困难重重

从平台实际数据存储情况来看，需要引入其他非关系型数据库，用于存储弱关系型的数据，以提升平台数据存储的适应能力。
可以加快新业务的开发速度，同时在业务变化时，降低对技术架构的影响。

从文档型数据库选型来看，MongoDB在性能和可靠性，维护成本上均满足我们的要求。

应用场景
MongoDB用于存储整个平台(quant,基金，期权OTC）的文档型数据，主要数据为json。

业务场景
-  新的业务需求中，如果不确定数据的关系，可以先将数据放在Mongo中，待业务迭代文档后，再考虑将关系型数据迁移到Mysql中。
-  历史的功能中的json自符，可根据重构计划，将数据从mysql中迁移到Mongo中。
- 目前cache中的数据都为json格式，部分数据可以从redis中迁移到Mongo中。同时整合cache数据，提高cache命中率，去除冗余cache。

技术要求
- MongoDB数据库应用于生产环境，需要具备HA特性，如果一个节点宕机，能够对外正常提供服务。
- 数据迁移到MongoDB中后，访问性能不应比从Mysql中提取json自符再解析的性能差。

部署流程
三台机器部署mongodb复制
192.168.10.87
192.168.10.88
192.168.10.119
以下内容除非特殊说明，三台机器全部都要执行
1. 部署docker
      
# 1.移除旧版docker
sudo yum remove docker \                  
docker-client \                  
docker-client-latest \                  
docker-common \                  
docker-latest \                  
docker-latest-logrotate \                  
docker-logrotate \                  
docker-engine
sudo mkdir /home/docker
# 2.添加docker仓库
sudo yum install -y yum-utils
sudo yum-config-manager \    --add-repo \    https://download.docker.com/linux/centos/docker-ce.repo
# 3.安装docker
# centos7
sudo yum install docker-ce-3:19.03.10-3.el7 docker-ce-cli-3:19.03.10-3.el7 containerd.io
# centos8
dnf install https://download.docker.com/linux/centos/7/x86_64/stable/Packages/containerd.io-1.3.7-3.1.el7.x86_64.rpm
sudo yum install docker-ce-3:19.03.10-3.el7 docker-ce-cli-3:19.03.10-3.el7


# 4.将下面内容写入/etc/docker/daemon.json，没有该文件就新建一下
{
  "registry-mirrors": ["https://docker.mirrors.ustc.edu.cn", "http://hub-mirror.c.163.com"],
  "insecure-registries": ["10.0.0.0/8", "100.64.0.0/10", "172.16.0.0/12", "192.168.0.0/16", "127.0.0.1/8"],
  "max-concurrent-downloads": 10,
  "log-driver": "json-file",
  "log-level": "warn",
  "log-opts": {
    "max-size": "10m",
    "max-file": "3"
    },
  "data-root": "/home/docker"
}
# 5.配置docker自启动，启动docker
sudo systemctl enable docker
sudo systemctl start docker
# 6.配置私有harbor仓库
# 使用k8s提供的dns
# vim /etc/resolv.conf
nameserver 192.168.10.126
# 配置登录harbor
docker login hub.mycapital.net
# admin，87c1d4e2db14422c5219ae2de903b5bd

2. 机器准备

sudo mkdir /home/mongo
cd /home/mongo
#分别为日志，存储和配置的目录
sudo mkdir logs db config
cd -
# 提供权限给rss(uid=1001/gid=1001)用户
sudo chown 1001:1001 -R /home/mongo

3. keyfile准备
由于需要配置多节点，节点之间需要keyfile进行认证，官方的推荐做法是使用openssl生成key，然后分别复制到各个节点来进行相互认证
生成key：

openssl rand -base64 756 > <path-to-keyfile>

然后复制该key到所有节点的相应文件夹：

/home/mongo/config

三个节点都要确保该文件的权限是400，且用户为1001

sudo chown 1001:1001 <path-to-keyfile>
sudo chmod 400 <path-to-keyfile>


4. 拷贝配置
拷贝如下配置文件到三个节点的相应目录

目录如下：
/home/mongo/config/mongod.conf


配置文件如下：
#vim /home/mongo/config/mongod.conf
# 三个节点应当保持一致
replication: 
    replSetName: mongo-rs0
    
# 不启动daemon模式，可以不用改
processManagement:
    fork: false
    
net:    
    bindIpAll: true
    port: 27017 # 默认为27017，没特殊原因不要修改
    maxIncomingConnections: 65536 # connection pool的最大连接数，可以自定义
    
storage:
    dbPath: /home/mongo/db
    wiredTiger:
        engineConfig:
            cacheSizeGB: 12 # 设置cache size
            
systemLog:
    destination: file
    path: /home/mongo/logs/mongod.log
    logAppend: true
    
security:
    keyFile: /home/mongo/config/mongo.key


三台机器均要启动服务，注意根据注释修改其中的配置参数

5. 使用docker部署mongodb

# 部署mongodb
# 改下name,三台 分别为my_mongodb_0,1,2,然后执行
sudo docker run -d \
 -v /home/mongo/:/home/mongo/ \
 --user 1001:1001 \
 --ulimit nofile=655350:655350 \
 --name my_mongodb_0 \
 --network=host \
 --restart always mongo:4.2.10 \
 --config /home/mongo/config/mongod.conf
# 上面命令中，
# -v映射目录，
# --user指定执行mongod的用户,
# --ulimit 配置了1001用户max open file,
# --name 指定用户名 
# --network=host 指定使用宿主机网络
# --restart always指定容器停止后自动重启
# mongo:4.2.10为镜像名
# --config /home/mongo/config/mongod.conf指定使用的配置文件


6. 设置replica set
进入主节点机器连接mongo数据库：
可从docker 进入

# 进入到主节点机器（87）
docker exec -it my_mongodb_0 bash 

进入mongodb

mongo --port 27017

运行以下命令：
其中“ip1”， “ip2”，“ip3” 分别为三台机器的ip地址
*注意，此处如果用dns域名的话会更好（如果有的话），ip地址存在变更的可能
rs.initiate( {
   _id : "mongo-rs0",
   members: [
      { _id: 0, host: "ip0:27017" },
      { _id: 1, host: "ip1:27017" },
      { _id: 2, host: "ip2:27017" }
   ]
})

运行

rs.status()

检查是否能看到所有节点的配置信息，查看选举出的primary节点（一般是你运行rs.initiate的机器），并进入到primary节点的mongodb

7. 创建admin用户以及clusteradmin用户
依然是在主节点上，运行如下命令：
创建admin用户
admin = db.getSiblingDB("admin")
admin.createUser({
    user: "<Your user name>",
    pwd: passwordPrompt(),
    roles: [{role: "userAdminAnyDatabase", db: "admin"}]
})
# 开启用户验证
db.getSiblingDB("admin").auth("frank", passwordPrompt())

创建集群管理用户

db.getSiblingDB("admin").createUser(
    {
    "user": "<Your user name>",
    "pwd": passwordPrompt(),
    roles: [{"role": "clusterAdmin", "db": "admin"}]
    })



也可以一个账户同时有多个roles，具体做法就是添加进上述roles后的list里面
关于所有mongodb 的roles，参考

https://docs.mongodb.com/v4.2/reference/built-in-roles/#database-user-roles


# 注意这里的权限划分比较细致，管理员并没有所有database的读写权限
如果不需要划分的非常细致，直接设置role为root

最后以管理员身份进入所有分节点上并运行如下指令：
以管理员身份进入：

mongo -u <your admin user name>

运行指令
rs.secondaryOk()



8. 在87机器上使用docker部署mongo-express
将下面参数中的ME_CONFIG_MONGODB_ADMINUSERNAME 以及
 ME_CONFIG_MONGODB_ADMINPASSWORD的值改为上述设置的admin账户密码即可
# 修改以下ME_CONFIG_MONGODB_ADMINUSERNAME和PASSWORD,填写，mongodb的账户密码
sudo docker run  -d \
--name my_mongo_express \
-e ME_CONFIG_MONGODB_SERVER=192.168.10.87,192.168.10.88,192.168.10.119  \
-e ME_CONFIG_SITE_BASEURL=/mongo_express \
-e ME_CONFIG_BASICAUTH_USERNAME=admin \
-e ME_CONFIG_BASICAUTH_PASSWORD=mycap123 \
-e ME_CONFIG_MONGODB_ADMINUSERNAME=lee \
-e ME_CONFIG_MONGODB_ADMINPASSWORD=123456 \
-p 8081:8081 --restart always mongo-express:0.54.0

# 以上
# ME_CONFIG_MONGODB_SERVER为mongodb的地址
# ME_CONFIG_SITE_BASEURL为exporess工作的url子路径
# ME_CONFIG_BASICAUTH_USERNAME 为exporess的访问账户
# ME_CONFIG_BASICAUTH_PASSWORD为express的访问密码
# ME_CONFIG_MONGODB_ADMINUSERNAME为mongodb的管理员名
# ME_CONFIG_MONGODB_ADMINPASSWORD为mongodb的密码

# 然后在100机器设置nginx反向代理/mongo_express到192.168.10.87:8081/mongo_express，以此让express能在公网访问

后期维护
监控和告警功能
使用定时任务监控监控容器运行状态
# 87
sudo docker inspect  my_mongodb_0 --format='{{/*读取容器状态*/}}{{.State.Status}}'
sudo docker inspect  my_mongo_express --format='{{/*读取容器状态*/}}{{.State.Status}}'
# 88
sudo docker inspect  my_mongodb_1 --format='{{/*读取容器状态*/}}{{.State.Status}}'
# 119
sudo docker inspect  my_mongodb_2 --format='{{/*读取容器状态*/}}{{.State.Status}}'
输出不为running时报警

如果有告警，则先通过企业微信发出， 后期将告警整合到https://docs.qq.com/doc/DSVVpSVNMQnpDSGlh?createTS=1602729451043&templateId=31227

