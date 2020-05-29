
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



## h5py

```python
import h5py
import tables
f = h5py.File('/data/hd/etf_option/tick_h5/10001312.h5', 'a')
print(f.keys())
```

something like that 
it should be noted that if OSError happens, it might be permission error
