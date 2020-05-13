## building wheel failed

- __error message__

```
error: unknown file type '.py' (from 'factor_store/detail.py')
    ----------------------------------------
ERROR: Command errored out with exit status 1: /home/frank/App/anaconda3/envs/etf_tick/bin/python -u -c 'import sys, setuptools, tokenize; sys.argv[0] = '"'"'/tmp/pip-install-pq9kmhnx/factor-store/setup.py'"'"'; __file__='"'"'/tmp/pip-install-pq9kmhnx/factor-store/setup.py'"'"';f=getattr(tokenize, '"'"'open'"'"', open)(__file__);code=f.read().replace('"'"'\r\n'"'"', '"'"'\n'"'"');f.close();exec(compile(code, __file__, '"'"'exec'"'"'))' install --record /tmp/pip-record-5m06_m5h/install-record.txt --single-version-externally-managed --compile Check the logs for full command output.

```

lack of cython package 

solution:

```
pip install cython
```

