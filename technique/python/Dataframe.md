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