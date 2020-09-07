## TTL cache 

- time to live cache
```python 
@ttl_cache
def expensive_operation(a, b):
    ...
    ...
    return SOME_RESULT

expensive_operation(xx, yy)
expensive_operation(xx, yy)  # prefer cached result
# ... 60 seconds later
expensive_operation(xx, yy)  # compute again


# or
@ttl_cache(2.0)  # cache the result in the next 2 seconds, default is 60.0 seconds
def expensive_operation(a, b):
```

this is a package that can be used


## LRU Cache

- least recently used 

```

```

## Making list hashable

```
a = [1,2,3,4]
s = {tuple(a): "list value"}

```
use tuple, because it's immutable


