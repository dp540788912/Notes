# TCP and UDP, socket programming 

- 表述能力欠缺，先用中文把

- 关于端口
```
一个端口只能绑定一个tcp的socket， 但是可以绑定多个udp的socket， udp和tcp可以公用一个端口
用select的时候，select会根据发过来包的协议来确定哪个描述符已经就绪

```

- 关于select
    - socket 可以理解成处理tcp/ip整个协议族群的数据结构
```
在绑定tcp socket之后，将socket加入到fd_set里面，select堵塞受到connect的连接请求之后，可以再次加入
新连接的socket fd，这样链接之后的请求可以根据链接对象的地址（ip/port）来进行识别，换言之

bind(master_fd, sockaddr)
|
fd_set(master_fd, read_fd)
|
select(fd_set)
    |
    receive connection:
        |
        new_fd = accept(master_fd)
            |
            fd_set(new_fd, &readfds)

这个过程可以在一条线程里处理很多tcp连接
但是注意select的连接总数是有限制的
epoll没有最大监听限制，会形成一种规模效应
```

select 的本质其实还是很像os的多任务管理系统


## how router works in a packet 

[how-router-works](http://www.firewall.cx/networking-topics/routing/181-routing-process.html)


## check network card 
```
sudo lshw -class network -short
```