## all the private variables with __

- \__all__

```python
# define in a py file and define which files can be imported through "from this import *"
__all__ = ['a', 'b']
```

- \__eq__
```python
# class function, define ==
class apple:
    def __eq__(b):
        return self.a == b.a
```

- \__lt__
```python
# means les than, the same as __eq__
```


- \__repr__

print(obj) will call this function _repr__ first, if this method failed 
print may hang for a long time, please watch the fucking up