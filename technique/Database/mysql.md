## local host and 127.0.0.1
```
If host is set to localhost, then a socket or pipe is used.
If host is set to 127.0.0.1, then the client is forced to use TCP/IP.
```

## mysql check table size in a database

```mysql
SELECT table_name AS "Table",
ROUND(((data_length + index_length) / 1024 / 1024), 2) AS "Size (MB)"
FROM information_schema.TABLES
WHERE table_schema = "<database_name>"
ORDER BY (data_length + index_length) DESC;
```


## mysqldump
So many options in this list

```
datahub "strategy_result" --result-file="/home/frank/Desktop/{database}-{data_source}.sql" --ssl-mode=DISABLE --opt --where="1 ORDER BY id DESC limit 1000" --set-gtid-purged=OFF --column-statistics=0
```

--set-gtid --> do not dump gtid
--column-statistics=0 --> do not use this function which may throw error


then restore, it should be noted that -D stands for database name

```
mycli -u root -P 3307 -p -D datahub < datahub-niubui.sql
```


## mysqlalchemy quick access

```python
from slqalchemy import create_engine

engine = create_engine("mysql://root:123@localhost:3306/database")
engine.execute("SELECTs  * from table_name")
```

## having and where 

having come with groupby, otherwise where is normal

sad

## session in database 

- session, transation and conversation 
  - session
    - 当一种语言的orm开始操作数据库的时候，需要session来作为一个上下文管理工具，一个session里面可能包含多个transaction，session是用来保证一次conversation的统一性，作为一个中间的cache



## check disk usage of mysql database 

```
select table_schema, sum((data_length+index_length)/1024/1024/1024) AS GB from i
                                   nformation_schema.tables group by 1;

```