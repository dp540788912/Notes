# definition 
- 非关系型数据库，c语言编写，基于key-value，广泛用于缓存，数据库，消息队列


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