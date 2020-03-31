2020 
### 研究回测带上order book id
## f


workspace:

## 个人与机构的区别
因子+因子企业版


## workspace

```
1、以前是给企业分权限，企业再下分
2、线上很多量化用户，希望其构成一个workspace，邀请好友写作
3、角色拥有权限组

confg: 因子跟踪
calc_options: 因子检验，计算的配置


## 开发环境
- rquser: http://192.168.10.53:30200/admin/login
- rquser api document https://yapi.ricequant.com/project/100/interface/api

- 测试环境192.168.10.53   root / Ricemap123
- 因子测试：
    curl -X GET http://192.168.10.53:30080/api/v1/factors/test -H "cookie: session=f786eac0-e8f6-46ac-bcae-27fc583d4eb8" -H "Content-Type: application/json"



## test 
```
- create one factor
curl http://dev:10005/api/v1/factors -H "Content-Type:application/json" -d '{"name": "test4", "workspace": "1234", "uid": 100}' -X POST

- get one factor
curl http://127.0.0.1:5000/api/v1/factors/12

- check list 
curl http://127.0.0.1:5000/api/v1/factors -H "Content-Type:application/json" -d 


- apply

curl http://127.0.0.1:5000/api/v1/factors/12/release -H "Content-Type:application/json"

```


- build docekr images

```
docker build --network host -t harbor.ricequant.com/test/factor-agent:2.0.0a69 --build-arg FACTOR_VERSION=0.2.0 --build-arg AGENT_VERSION=2.0.0a69 .
```

curl -X POST http://192.168.10.53:30080/api/v1/factors -H "cookie:session=f786eac0-e8f6-46ac-bcae-27fc583d4eb8" -H "Content-Type: application/json" -d '{"code": "from rqfactor import“}' -d '{"name": "test", "config": {"pool": null}}'

- open rqdatad
```
nohup rqdatad -c /root/rqdata-citis2019/internal.yaml  --port 16071 > my_out.txt 2> foo.err < /dev/null &
```

