# general
----

## remove files except certain files

```
rm -v !("file1" | "file2")
```
- -v means verbose, print log 


## set up printer 

[printer](https://www.linuxbabe.com/ubuntu/set-up-cups-print-server-ubuntu-bonjour-ipp-samba-airprint)

## memeory use black technique

```bash
ps -e -orss=,args= |awk '{print $1 " " $2 }'| awk '{tot[$2]+=$1;count[$2]++} END {for (i in tot) {print tot[i],i,count[i]}}' | sort -n
```

## compgen

- list commands
```
-c # list all the commands you can run 
-a # list all the alias you can run 
```

## cpu info 

- list all the cpu information
```
lscpu 
```


## fg 

- go back to your previous progress on a process 
for example
```bash
# you shut down a progress by ctr + z
# then you can awake it by using fg 
```

## static link lib
- in linux, it's always .a .so
    - .so --> dynamic 
    - .a --> static 
- g++ -c hello.cpp 
    - don't execute link, only to static file
- g++ hellp.cpp speak.cpp -o result
    - link two source file to a single executable file

```bash
# 静态链接将所有文件，将所有相关依赖文件.o打包成一个可知性文件
# 动态库不会在编译时链接进目标代码，而是运行时才被载入
```


## zip a folder

```
zip -r [output_file] documents
```

## unzip all the zip files in a directory

```
unzip '*.zip' -d dest
```

## pgrep 

```
pgrep redis-server 
```

directly display the process id


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

- -P can show process info, if you want to kill a process, use this 
- close a port listened by a process 
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

### find you are not root user when you want to save result 
```
:w !sudo tee %
```

### advanced operations

- edit each line at the beginning in group

```
1. crtl + v to enter block visual mode (in pycharm, it is replaced to ctrl + shift + v)
2. capital 'I' to insert, lower case 'c' to replace, capital 'A' to append
3. press ESC to apply the change  
```

before:
```
pick 84e78850e add cron job for factor, need more detail
pick 61e0f5963 use common path
pick 0407d883f debug
pick fd47af306 add save path
pick b1120a5d0 api modification
pick 55bd18853 add return fields
```

after use 'c' to replace 
```
squash 84e78850e add cron job for factor, need more detail
squash 61e0f5963 use common path
squash 0407d883f debug
squash fd47af306 add save path
squash b1120a5d0 api modification
squash 55bd18853 add return fields

```



----

- config file of vim is /etc/vimrc
- to customize vim, add ~/.vimrc and add lines 
- G to forward to bottom line 

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

it should be noted that -r option could check all files in given directory, very useful 


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
t

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

- define shift + crtl = s + c
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

1. n for next, and shift + n for previous 
 

## cut

cur -d "delimiter" if (field name)

file is like:
```
aaaa vvvvv ddddd
bbbbb dsad sgfgfg
cccc fdfd cdfs
```

```
cut -d " " -f 1 file:
```
out put will be `

```
aaaa
bbbbb
cccc
```

* an example 

```
sudo kill -f $(ps aux | grep python | tr -s ' ' | cut -d " " -f2 | tail -n 7)
```

- tr -s means squzee charater with repeated sequence to a single occurrence of that character 


## swap 

used when RAM run out of memory 
it's related to virtual memory technique, it should be considered later 

## ubuntu command line proxy tools 

```
    proxychains3 wget http://dadasdasrscfsffsdfsdfsdf
```

wget command will use proxy

## telnet 

shut down telnet in terminal 

```
ctrl + ]
or simple type q

```

# TCP and UDP 

```md
Process of TCP server

- :socket create socket obj 
- :bind set up AF_INET(ip protocol), sockstream(TCP), and port
- :listen listen on the port, you will get a listen socket, which is different from client socket that you will obtain later 
- :accept on the port, block the process, it will return the client_socket
- :recv: start to recieve data from client end
- :in python, client needs to shut down client socket to indicate the data exchange is over 
- :you can close listen socket once you establish a connection with client
- :you can obtain information about client 

```

- htons, htonl, and etc.
    - this kind of function convert host byte order to network byteorder
        - eg. short is 16bit integer, whereas long is 32bit integer, the order is called some fucking "big-endian", "little-endian", don't need to dig too deep



## c++ session 

- virtual function 

```
1、c++ 类有个存储地址，对象调用方法会直接调用这个地址的方法

obj =========>   Class 0xfc1c1f3d

2、如果内部有虚函数的话，每个对象都有保有一个虚函数表
与指针类无关，直接调用对象的类中的虚函数表，由此实现多态

3、普通函数的载入顺序一般在virtual之前，比如父类有个虚函数a，自类有个同名实函数a，父指针指向实例化子对象，调用a引用的是子函数里的实函数a

顺序：
Base.true_method --> Derive.true_method --> Derive.virtual --> base.virtual

```

## yum 更新源

```
mv /etc/yum.repos.d/CentOS-Base.repo /etc/yum.repos.d/CentOS-Base.repo.backup
curl -o /etc/yum.repos.d/CentOS-Base.repo http://mirrors.aliyun.com/repo/Centos-7.repo
sed -i "/mirrors.aliyuncs.com/d"  /etc/yum.repos.d/CentOS-Base.repo
sed -i "/mirrors.cloud.aliyuncs.com/d"  /etc/yum.repos.d/CentOS-Base.repo
yum clean all
yum makecache
```
