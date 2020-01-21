## change the user of a certain command 

you can get rid of typing sudo every time 

1. check where command is 
```
which docker 
```

2. change user 

```
sudo chown frank:frank /usr/bin/docker 
```


## mkdir recursively 
```
mkdir -p /root/project/caoni 
```
if there is no parent dir, it will be created automatically with -p option
