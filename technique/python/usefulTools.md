
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




## change pip source to douban source

- change ~/.pip/pip.conf index-url to douban 

- douban source
    -  https://pypi.doubanio.com/simple