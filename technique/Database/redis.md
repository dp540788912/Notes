# definition 
- 非关系型数据库，c语言编写，基于key-value，广泛用于缓存，数据库，消息队列

# big picture of redis

- redis-cli, means redis command line interface

## 1. startup

- config redis, put config file in /etc/redis/config.conf
- run redis server:
```bash
redis-server /etc/redis/config.conf
# demonize yes in the file
```
you can also use systemctl to manage redis

## 2. get to know

- redis is case insensitive
- MSET, M stands for multiple action, eg:
```redis
MSET a1 v1 b1 v2
```

- hashset

```
HSET k1 f1 v1
```
pretty much like python nested dict, 
```python
dict = {
    'k1': {
        'f1': 'v1'
    }
}
```

- HMSET, M stands for multiple
    - noted: result in redis-cli is tricy, key and value are put in different lines


## data types

- sets, hashes, lists, strings

- lists is lined-lists

## redis.py

- set decode_response to True, it will automatic transfer from byte to string




## redis pipeline 
    pack a set of command, reduce the network latency 
    test:

```bash
redis-benchmark -t get,set -q
# test normal case
redis-benchmark -t get,set -q -P 16
# this simulate a pipeline of 16 commands 
```

    if you need to execute multuiple redis command in one step, the best method is to wrap them in a packet, which is the pipeline method 


## redis expose port to all others

1. edit config file
    - protected_mode yes --> no
    - comment "bind 127.0.0.1"

2. systemctl restart redis.server

3. close firewalls if where exists any 

same as mysql server


## cli means "command line interface"



