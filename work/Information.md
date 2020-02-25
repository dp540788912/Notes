# Things to refer

## production server address

address|account|pwd
:---|:---|:---
192.168.0.109|root|g8wg^#7dgk8
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

