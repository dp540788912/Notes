## local host and 127.0.0.1
```
If host is set to localhost, then a socket or pipe is used.
If host is set to 127.0.0.1, then the client is forced to use TCP/IP.
```

## mysqlalchemy quick access

```python
from slqalchemy import create_engine

engine = create_engine("mysql://root:123@localhost:3306/database")
engine.execute("SELECTs  * from table_name")
```

## having and where 

having come with groupby, otherwise where is normal


## session in database 

- session, transation and conversation 
  - session
    - 当一种语言的orm开始操作数据库的时候，需要session来作为一个上下文管理工具，一个session里面可能包含多个transaction，session是用来保证一次conversation的统一性，作为一个中间的cache



## check disk usage of mysql database 

```
select table_schema, sum((data_length+index_length)/1024/1024/1024) AS GB from i
                                   nformation_schema.tables group by 1;

```