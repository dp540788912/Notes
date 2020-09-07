# whatever I found, I write here 

## c++ exit and return 

- return stops a function
- exit stops the whole process, the param in exit indicates what parent receives


## fork

```c++
pid = fork()
// in parent process: return the pid of it's child process created by this func
// in child process it returns 0, so
if(pid == 0){
    // in child process 
} else if(pid > 0){
    // in parent 
} else {
    // failed create child process 
}
```