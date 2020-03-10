# Tools

## General

- Ascii code graph
![ascii](../image/ascii.png)


- [SSH tutotial](./SSH.md)

## Python 

> - [Python function runtime visulized tool: snakeViz](https://jiffyclub.github.io/snakeviz/)

docker run -itd --restsart always --name matlab-vc -v "$PWD":/project -p 8888:8888 python:3.7.5-alpine3.10 python /project/matlabVC/__main__.py -p 8888 -c /projcect/congig.yaml


## establish a vpn server, docker

```
ocker run --restart always -itd --name ssserver -p 6443:6443 -p 6500:6500/udp mritd/shadowsocks:3.3.3-20191229 -m "ss-server" -s "-s 0.0.0.0 -p 6443 -m chacha20-ietf-poly1305 -k testchacha654321" -x -e "kcpserver" -k "-t 127.0.0.1:6443 -l :6500 -mode fast2"
```
