# basic operation

## Write a docker file
almost the same as bash command, watch out the syntax 

eg:
```Dockerfile
FROM harbor.ricequant.com/ricequant/python36_base:0.10
MAINTAINER Frank <deng.pan@ricequant.com>

RUN yum install -y make \
    openssl-devel \
    gcc \
    gcc-c++ \
    python-devel \
    kernel-devel \
    libxslt-devel \
    libffi-devel \
    snappy-devel \
    csnappy-devel \
&&  yum clean all \
&&  rm -rf /var/cache/yum \
&&  localedef -c -f UTF-8 -i en_US en_US.UTF-8

 

RUN pip install --upgrade pip \

&&  pip --no-cache-dir install \
    -i https://pypi.tuna.tsinghua.edu.cn/simple/ \
    requests \
    cos-python-sdk-v5 \
    click \
    python-snappy \
    Pyyaml \
    gevent \
    Logbook \
    setproctitle \
    msgpack-python \
    config 

RUN mkdir -p /root/project
COPY config.yaml /root/project
COPY matlabVC /root/project

```


## build a image based on Dockerfile

```bash
docker build -t imagename:edition .
```
replace your own image name 

## start a image 

it should be noted that every time you start container from a image, all the modification you have done with 
this container so far will be lost unless you never delete the container you created from this image

```
docker run -it -p 8080:8080 --name contianer_name imagename [YOUR CMD]
```
* -d run without hangup, same as nohup 

## enter a docker contianer 

```
docker exec -it container_name/container_id bash/sh
```
bash is prefered
id is randomly generatd by docker when you create your container 


## stop a running container

```
docker stop name/id/hashcode
```

## remove a stopped contianer
you will lost all of your works you've done in this contianer, be careful 
```
docker rm name/id/hashcode
```



## trap

### slash \
+ in dockerfile, be careful when you use \ (backslash)
``` dockerfile
Run yum install sql \dir1 
 |
 |---file1
 |---file2
 |---file3
mongo \
redis 
```
stop now, one more bachslash may cause unpredictable problem as it runs 


### COPY
not actually like the bash syntax 
will copy the content in a dolder instead of the whole folder, which means the dir name may be lost:

```
COPY dir1 /Dst
```

assume in dir1:
```
dir1 
 |
 |---file1
 |---file2
 |---file3
```

then in the Des:

```
Des 
 |
 |---file1
 |---file2
 |---file3
```

dd


## open a sql server
```
docker run -itd --restart always -e TZ=Asia/Shanghai -v /etc/localtime:/etc/localtime:ro -e MYSQL_ROOT_PASSWORD=root -p 3306:3306 --name mysql mysql:5.7.23
```


## Kubectl

### get po about rqdata
```
kubectl get po -n rqdata
```

### get logs 
```
kubectl logs -n rqdata rqdatad2-http-new-574ff6c97f-bsljx
```

### get config file 
```
kubectl describe configmaps -n rqdata rqdatad2-http-new-config
```
