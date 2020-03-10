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
