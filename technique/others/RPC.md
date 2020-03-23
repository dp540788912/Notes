## RPC service

* service that makes running a remote service like running locally
    - RPC本质为消息处理模型，RPC屏蔽了底层不同主机间的通信细节，让进程调用远程的服务就像是本地的服务一样

* RPC 框架适用于大企业，内部调用非常多的场景，采用tcp/ip协议，效率会比http协议高
    - 相对而言，http的好处是，开发迭代更快，开发更方便，接口不多的话比较适合使用


* RPC 通讯方式可以采用nio或者bio，具体根据情况而定

* RPC 传输数据一样应用序列化技术json或者xml

