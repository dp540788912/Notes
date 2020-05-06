## local host and 127.0.0.1
```
If host is set to localhost, then a socket or pipe is used.
If host is set to 127.0.0.1, then the client is forced to use TCP/IP.
```

## mysqlalchemy quick access

```python
from slqalchemy import create_engine

engine = create_engine("mysql://root:123@localhost:3306/database")
engine.execute("SELECT  * from table_name")
```