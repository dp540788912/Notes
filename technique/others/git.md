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
eg: git push -d origin frankLee
```

__push a newly created local branch to remote__
```
git push -u origin frankLee
```

__checkout a remote branch__

```
git checkout --track <remote branch name>
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

__push a new branch to remote__

```
git push -u origin new_branchx
```

__push new branch to remote__
```
 git push --set-upstream origin citics_2019
```

__reset to a previous edition hardly__

this will delete all the work you have done since then, be careful with the --hard arg
```
git reset --hard 38208ca4252982fbe28e0799f83df9055c56d29b
```
after doing reset, force push to the remote 