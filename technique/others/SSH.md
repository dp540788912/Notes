# SSH tutorial

## remote server exempt for password
1. generate public keys ~/.ssh

It may ask you where to store the key, just press enter
```shell
ssh-keygen -t rsa 
```

2. copy public key to remote server

use either
```
ssh-copy-id usr@remoteAddress
```
this method may fail since ```ssh-copy-id``` is unstable. when this happens:

* copy rsa file yourself 
```
scp ~/.ssh/id_rsa.pub usr@address:~/.ssh
```

* append it to authorized_keys
```
ssh usr@address
cat ~/.ssh/id_rsa.pub >> ~/.ssh/authorized_keys
```

then exit server, next time it will not request a password

* if you are asked to enter a password to make unlock your private key, just enter the passphase you set after -p 

* difference between && and ; when run bash 

; means two commands run irrespectively

```bash 
true ; echo OK
# OK
false; echo OK
# OK
```

&& means when command1 failed, command 2 will not run
```bash
true && echo OK
# OK
false && echo OK
# [no output]
```



## SSH script 

- one line command 

```bash 
 ssh myusername@remotehost 'ls -lha'
```

- multiple line commands

```bash
ssh -t myusername@remotehost << "ENDSSH"
cd /home/myusername
ls -lha
ENDSSH
```





