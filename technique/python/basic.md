## change download source temporarily

add the line below every time install by using pip 

```
-i https://pypi.tuna.tsinghua.edu.cn/simple
```


## with open(filename, 'w') fucking shit 

``` 
in some situation, the system can't recognize path like '~/folder1/folder2'
use the '/root/....' format, fucking dump python interpreter 
```

## when you want to open a file in a certain dir

check if there is dir existing, if not, create one 
```python
filename = ...
dirname = os.path.dirname(filename)
if not os.path.exists(dirname):
    os.makedirs(dirname)
```

## r, u, b, f


## get the path of current folder 
```python
IMPORT_ROOT = os.path.dirname(os.path.dirname(__file__))
sys.path.append(IMPORT_ROOT)
```


# shortcut 
```
Command + j = choose shortcut for if __name__ == "__main__"
```


## loop with index 

```python
for i, date in enumerate(dates):
    pass
```


## throws exception then check the detaik 
```python
 except Exception:
            import traceback
            print(traceback.format_exc())
            self.__dict__ = {}
```


## arexit
```python
import atexit
atexit.register(lambda: scheduler.shutdown())
```
the lambda func will be executed when the program terminates 

## time time
```python
time.time()
# convert to readable
time.ctime(_)
```
Pythom time method time() returns the time as a floating point number expressed in seconds since the epoch, in UTC.

- get timestamp in seconds
```
time.monotonic()
```
compared with time.time() this is less in memory 


## safest method to check if dict can get a object

```python
monitor = object()
val = dic.get('key', monitor)

if val == monitor:
    ...
    ...
    ...
```

it's the safest method


## functiona tools

### *partial
```python
base_convert = partial(int,base=2)
base_convert('10010')
18
```
to preset value for certain params

