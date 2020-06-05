# general
----
## zip a folder

```
zip -r [output_file] documents
```

## unzip all the zip files in a directory

```
unzip '*.zip' -d dest
```



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

## check storage usage linux 

```bash
df -H
```

## check directory disk space usage

```
du -sh /dir
```
- du means disk usage?
     - niubility

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

this can be written in bash_aliases
```
nohup sh /home/frank/App/pycharm-2019.2.3/bin/pycharm.sh  >/dev/null 2>&1 &
```

## check version 
```
uname -a
```


## sed

- delete a line with specific string 
```bash
sed -i '/pattern to match/d' ./infile
```


## touch with general expression 
```
touch dir1/file{1...100}
```

- create 100 files 


## rsync 

* use algorithm to sync files, only send the different part from one end to another, can be used both remotly and locally




## Vim
----

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
-v exclude a pattern

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



## update alias 
```
// change bash alias file 
// type
source ~/.bash
```


## use stream as args 

- xagrs
```
find / -name "dashuaibi" | xargs rm -f 
```

delete all the files from the find command 


## unset 

- delete env variable

```
unset var_Name

```

# file system 
----


- /etc
    - configure file 

- /var
    - log

- /dev 
    - device 


## unrar 

parameters

| command | description |
:-|:-|
e  | extract without path 
x  | extract with path

| switch | description |
:- | :- | 
-p[password] | enter password(right after -p, no space needed, this is so fucking shit)
-r | recursive 

- example

```bash
unrar e -r -o- -pwww.jinshuyuan.net  ./*.rar ~/Desktop/ETF5_all/ 
```

## install package deb 
```
dpkg -i path/to/file
```




## regular expression in shell 

```bash

# list all lines contains 'a'
cat sample | grep a

# start with 'a'
cat sample | grep ^a

# end with 't'
cat sample | grep t$

# appears exactly 2 times
cat sample | grep -E p\{2}

# 'a' precesdes 't'
cat sample|grep "a\+t"

```

- prompt after rm 

```
rm -i {file}
```

this command will prompt when delete file


# shortcut

## basic


## terminator(ubuntu)

- shift + crtl = s + c
- s + c + e, s + c + o, split window vertically or horizontally
- s + c + w, close window
- s + c + t, open new tab


## install virtual machine 

- first install virtualbox 
```
sudo apt install virtualbox 
```

- then download ios file from official site (important)

- set up virtualbox, run 

- install guest additions, to calibrate seamless mode and full screen mode 
```
sudo apt-get install virtualbox-guest-additions-iso

```



## change theme 

[gnome-tweak-tools](https://www.cyberciti.biz/faq/change-theme-in-ubuntu/)

## apt install -y 

-y means yes as default. it will not prompt

## less

1. 