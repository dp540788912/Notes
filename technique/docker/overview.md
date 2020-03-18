

# Get Start 

## overview

简单来说，docker就是将一个操作系统运行所需的最小部分封装在一块独立内存里，使得在任何支持docker的操作系统下都能以最小的代价运行其他操作系统。这块运行着另一个操作系统的小块内存称为docker容器

docker容器里运行的操作系统独立于主机的操作系统，同时docker提供了容器内和外部“交流”的渠道，比如可以绑定docker容器的端口和主机的端口，这样发送到主机端口的信息能在docker容器内部被处理

docker公司的文档里面的总结很到位：
> Containers are lightweight because they don’t need the extra load of a hypervisor, but run directly within the host machine’s kernel

放弃了操作系统的管理模块，以及用户界面这些，直接运行在主机内核。当然这样的机制是不可能指望有生动的可操作的桌面给你用了，只能通过命令行在docker容器内操作。本身shell功能非常完善的linux系统自然成了docker container使用最多的操作系统

可以理解为一种更加轻便的而且没有用户界面的虚拟机

另外，虽然说十分轻便，但根据具体业务需求，可以进行深度定制，建立属于你独有的docker容器，自己命名，自己配置内容。这种定制化的容器被称为docker镜像

docker技术等于把操作系统抽象成了一个app，安装docker image的过程可以抽象为安装一个软件，最后使用docker就好比在使用一个app一样，一台电脑能开许多app，app之间互不影响，又能通过某些渠道进行数据交换

```

host computer ----> docker image1: linux/python3
                    (运行python程序的linux环境)

              ----> docker image2: linux/g++
                    (运行c++程序的linux环境)

              ----> docker images3: wondows
                    (运行windows程序)

              ----> docker images4: macOS
                    (运行mac上的程序)
```

是的，一台电脑上能够同时使用这么多不同操作系统的程序，这已经很不可思议了，更不可思议的是你只要事先打包好了docker image并发布到了网上，在任意一台支持docker的主机上用几条命令行就能运行起来，不用配置参数，不用配置环境，不用管兼容性问题


## significance of using docker

docker是最近几年火起来的概念，在我的理解里，他两个最重要的功能：
1. 全面提升开发效率
2. 增强软件的可移植性

前面说过，通过打包好的docker image，你基本能实现傻瓜操作运行各种平台的软件，这对开发效率是质的提升

特别是对于python这种对于操作系统依赖很高的解释型语言，简直是福音

相对的，java程序对docker的依赖程度就不是那么高了，java在设计之初就是遵循的

```
one time compile, runs everywhere
```

java在程序和操作系统之间用了一个类似于中间件的东西，叫jvm，java virtual machine。每种操作系统只开发与其相通的jvm，jvm与java程序的交流保持一致。

另外java的第三方库不是像python内置于环境里，而是以包为导向

所以docker对python来说是雪中送炭，对java来说是锦上添花

## docker 的架构

docker 建立在3个linux内核的基础上
* namespace，相同类型模块使用公用的namespace，用于区别不同类型模块的同名类
* 资源分块技术
* 文件系统