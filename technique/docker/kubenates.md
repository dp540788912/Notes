## check config 
```bash
kubectl get configmap -n factor factor-agent-config -oyaml
```

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