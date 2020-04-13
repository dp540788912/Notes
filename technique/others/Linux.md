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


## check port usage 

```
sudo lsof -i -n -P | grep 5000
```

## nohup 
```
nohup rqdatad -c /root/rqdata-citis2019/internal.yaml  --port 16071 > my_out.txt 2> foo.err < /dev/null &
```

## check version 
```
uname -a
```

## shell script 
```bash
# 1. when a variable contains space, use double quotes, x="das ddf"

```
### grep 

```
grep -rni 'this' filename
```
-r recursive 
-n show line number 
-i ignore case 
-e expression, can use mutiple times


### expr
```
expr 1 + 3
```

out put will be 3, watch that there should be spaces between them


## authentication and permission 

```bash
chmod 755 filename
```
7 = 4 + 2 + 1, means write, read, exec 
you can use a+x means anyone can exec



