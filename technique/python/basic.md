# Table of content 
1. [basic](#basic)
2. [shortcut](#shortcut)
3. [tricky part of python](#tricky\ part\ of\ python)

# basic

## file descriptor, fd, fsync, flush 

f.flush copy cache in python to OS

f.fsync actuallu writes to disk 

## importlib, walkpackage

```python
import importlib
import pkgutil
import endpoints
{"day": true, "end": "20500101", "desc": "", "name": "t0_f_v4tar_202009301402", "noints.__path__, endpoints.__name__ + '.'):
    pass
```

- function walk_package to walk package

```python
def walk_packgae(path_to_search, module_name_represented_in_result):
    pass


```





## celery 

- delay and apply_async 

```
- delay is preconfigured and simpler 
- apply_async can be more flexible
```

## nginx  

```
location ^~ /api/v1/platform/internal/config/future_risk_account {
        proxy_http_version 1.1;
        proxy_pass http://192.168.4.55:18887; 
}
location ^~ /api/v1/platform/file_upload {
        proxy_http_version 1.1;
        proxy_pass http://127.0.0.1:16010
}

location ^~ /api/v1/platform/risk/publish {
        proxy_http_version 1.1;
        proxy_pass http://127.0.0.1:16010
}

```

## KeyboardInterrupt

- It inherits from BaseException, which is also inherited by Exception 
    which means, only catch Exception cann't catch KeyboardInterrupt correctly.
    This is because you don't want to mess up with your main program

- correct practice

```python
try:
    main()
except KeyboardInterrupt:
    # do stuff 
    pass
except Exception:
    # do stuff
    pass
```

## pickle 
- dump python object to binary and loads it as object 

```python
import pickle 
a = [1,2,4,6,7]
ap = pickle.dumps(a)
ar = pickle.loads(ap)

a == ar 
```



## python debug

- basic use 

```python
import pdb; pdb.set_trace()
```
this will prompt in a command line and share context with current program

## build wheel 
```bash
python3 setup.py sdist bdist_wheel
```
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

## when you want to open a file in a certain dirasync def some_async_generator(<arguments>):
            <setup>
            try:
                yield <value>
            finally:
                <cleanup>
```pythonmethodName

## get the path of current folder 
```python
IMPORT_ROOT = os.path.dirname(os.path.dirname(__file__))
sys.path.append(IMPORT_ROOT)
```


## join

- put an interval between every two adjacent elements in a list

```python
l = [i for i in "abcd"]
" interval ".join(l)
# output:
# a interval b interval c interval d

```

## change environment variable 

```python
os.environ["DEBUSSY"] = "1"

```

it should be noticed that env variable is string, so don't use int 



# shortcut 
```
Command + j = choose shortcut for if __name__ == "__main__"
```

async def some_async_generator(<arguments>):
            <setup>
            try:
                yield <value>
            finally:
                <cleanup>
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



## h5py and tables

this two could cause so fucking serious problems if you installed with pip
what you need is:

```
conda install pytables
conda install h5py
```


# tricky part of python 

- Variables shadows in loop
```python
i = 3
for i in range(19):
    pass

print(i)

```

in the case above. i in loop will shadow i defined before

- python fails to recognize '~' in path 

```python
import sys  
sys.path.append("~/Desktop")
# It's wrong, python doesn't know your home dir

sys.path.append("/home/yourid/Desktop")
# use full absolute path is prefered

```


## join two paths

usually use os
```python
import os 
os.path.join(dir1, dir2)
```

## compile problems

1. one possible solution is to change python or package version 

##  \__new__ and \__init__

- __\__new\____ always happens before __\__init____, __\__new\____ is used for create new instance while __\__init____ is used to initialize new instance

- __\__new\____ is static class, and __\__new\____ must be called after instance has been created 
