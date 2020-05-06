## how to merge, concat, append


## pymongo insert dataframe to mongodb 

usually, dataframe needs to convert to a list of dict obj
such as 
```
[ {a: 1, b: 44}, {a: 2, b: 343}, {a: 3, b: 343} ]
```
the solution is:

```
df.to_dict('records')
```


## print out of a dataframe 

```
pd.set_option("max_columns", 999)
pd.set_option("max_rows", 5)
pd.set_option('display.width', 1000)
```

display.width stands for how many columns displayded in one row
max columns stands for total columns displayed


## pandas create new columns based on other colmumns 

```python
"""
         a   b
yo      aa  a1
yoyo    bb  b2
yoyoyo  cc  c1
"""
# df = above 
# if you want to concat a and b

df.apply(lambda row: row['a'] + row['b'], axis=1)

# result should be:
"""
yo        aaa1
yoyo      bbb2
yoyoyo    ccc1
"""

```


## loop dataframe 

```python 
import pandas as pd 
df = pd.DataFrame()

"""
df:
       a    b  c
w     11  111  1
wc    22  222  2
wcn   33  333  3
wcnn  44  444  4

"""
```

- loop1:

```python 
for i in df:
    print(i)
"""
loop columns, results will be:
a
b
c
"""
```


## numpy check nan

- use np.isna to check an if element in an iterable item is nan
- use np.all to check if all the element in an iterable item is true

```python
np.all(np.isnan([1,2,3,4, float("nan"), np.nan]))
```