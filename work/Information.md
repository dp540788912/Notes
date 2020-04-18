# Things to refer

## production server address

address|account|pwd
:---|:---|:---
192.168.0.109|root|z
| |rice|84j84j302ijs3

## Jenkins serverr address

status|address|account|pwd
:-|:-|:-|:-
internal|<http://192.168.10.64:8080/>|rice|map
production|<http://192.168.0.161:8000> | rice | map



## look up investment stratagy 

```
github rqalpha
```

# kubectl 
## get po about rqdata
```
kubectl get po -n rqdata
```

## get logs 
```
kubectl logs -n rqdata rqdatad2-http-new-574ff6c97f-bsljx
```

## get config file 
```
kubectl describe configmaps -n rqdata rqdatad2-http-new-config
```


## docker build
```
docker build --network host -t harbor.ricequant.com/test/factor_agent:2.0.0a6 --build-arg VERSION=2.0.0.a6 .
```

## pypi
```
python setup.py sdist upload -r rq
```

### install 

```
pip install  --extra-index-url https://ricequant:RiceQuant77@pypi.ricequant.com:8080/simple/

```

## 预发布环境标配：
```
export RQ_ENV=production
export RQ_CLOUD=pre
export RQDATA_CONF=/etc/rq/rqdata.yaml
export RQDATAC_CONF=tcp://rice:rice@172.18.0.17:16010
```