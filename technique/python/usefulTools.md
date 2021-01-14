
## pydantic

- logic 

### with pre = True

* only given values from outside exists

validation will not start

you can change values to affect the actual fields

withou pre=True

validation will be called 

eg:
```python
class StrategyValidationSchema(StrategyCreate):
    r_create_user_id: int = Field(...)
    r_update_user_id: int = 0
    start_date: str = ""

    # underscore_private_attrs
    _detail_to_table: dict = {
        # field name in detail -> field name in table
        "start": "start_date",
        "end": "end"

    }

    @root_validator(pre=True)
    def pull_detail_to_model(cls, values):
        for k, v in cls._detail_to_table.items():
            if k in values['detail']:
                values[v] = values['detail'][k]
        return values

    @validator("r_update_user_id", pre=True, always=True)
    def init_update_user(cls, v, values):
        if v == 0:
            return values['r_create_user_id']

    class Config:
        underscore_attrs_are_private = True

```

## tqdm

```python
from tqdm import tqdm as tqdm_base


def tqdm(*args, **kwargs):
    if hasattr(tqdm_base, '_instances'):
        for instance in list(tqdm_base._instances):
            tqdm_base._decr_instances(instance)
    return tqdm_base(*args, **kwargs)
```

- a progress bar tools, really awesome


## snakeviz 

- [Python function runtime visulized tool: snakeViz](https://jiffyclub.github.io/snakeviz/)
- usage 
```bash
python -m cProfile -o program.prof my_program.py
snakeviz program.prof

```



## change pip source to douban source

- change ~/.pip/pip.conf index-url to douban 

- douban source
    -  https://pypi.doubanio.com/simple



## h5py

```python
import h5py
import tables
f = h5py.File('/data/hd/etf_option/tick_h5/10001312.h5', 'a')
print(f.keys())
```

something like that 
it should be noted that if OSError happens, it might be permission error


## pycharm 

### find in path
    ctrl + shift + f is "search a word in all files"