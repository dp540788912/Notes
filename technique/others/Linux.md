# general

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


# Vim
- config file of vim is /etc/vimrc
- to customize vim, add ~/.vimrc and add lines 

- command:
```
: set encoding=utf-8

```

- in normal mode
```
p: paste current line 
dd: delete current line 
yy: copy current line 
```