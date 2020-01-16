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


