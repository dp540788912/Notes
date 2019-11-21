__abort merge__
```
git merge --abort
```

__check out a remote repository__
```
git fetch 
git checkout origin/branch-name
```
__delete a remote branch__
```
git push -d <remote branch name>
eg: git push -d origin/frankLee
```

__push a newly created local branch to remote__
```
git push -u origin frankLee
```

__checkout a remote branch__

```
git checkout -t <remote branch name>
```

__list all currently configured remote branch__
```
git remote -v
```

__create neww branch and switch to it__
```
git checkout -b <branchname>
```

__push all to your remote branch__
```
git push --all origin
```


__store password and usename to avoid typing them everytime__

```
git config credential.helper store
// then do push 
```

