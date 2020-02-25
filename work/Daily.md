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
- rquser: http://192.168.10.53:30200/admin/rquser
- rquser api document https://yapi.ricequant.com/project/100/interface/api

- 测试环境192.168.10.53   root / Ricemap123
- 因子测试：
    curl -X GET http://192.168.10.53:30080/api/v1/factors/test -H "cookie: session=f786eac0-e8f6-46ac-bcae-27fc583d4eb8" -H "Content-Type: application/json"