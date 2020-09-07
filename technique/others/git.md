## git 

__revert a commit__

[understand revert](https://gitirc.eu/howto/revert-a-faulty-merge.html)


__git symbol, range selection__

[git tool](https://git-scm.com/book/en/v2/Git-Tools-Revision-Selection)

__when you regret after you did "git reset --hard "__

git will clear your commit after a month

you can still get your commit back even after you hard reset those 

```bash
git reflog # this will show your history commit, find the commit you  want to go to 
git reset --hard 1df23ddf # just a little taste
```
So don't worry about some shitty operation

say it out loud: Git niubi

__change default editor to vim__

git config --global core.editor "vim"


__use git rebase to merge multiple commit to one__


1. git rebase -i HEAD~n (n is the number of commit you want to include, HEAD~1 is the commit before HEAD)
2. it will prompt in a editor: 
```
pick 84e78850e add cron job for factor, need more detail
pick 61e0f5963 use common path
pick 0407d883f debug
pick fd47af306 add save path
pick b1120a5d0 api modification
pick 55bd18853 add return fields
```
change this to 
```
pick e9951b980 amend part of detal
squash 84e78850e add cron job for factor, need more detail
squash 61e0f5963 use common path
squash 0407d883f debug
squash fd47af306 add save path
squash b1120a5d0 api modification
squash 55bd18853 add return fields
```
save and quit 
3. it will prompt you in another editor interface
```
# This is the 1st commit message:

add api

# This is the commit message #2:

add api

# This is the commit message #3:

amend part of detal

add cron job for factor, need more detail

```
change the message to whatever you want 

4. save and quit 
you are done

__abort merge__
```
git merge --abort
```

__check out a remote repository__
```
git fetch 
git checkout -t origin/branch-name
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