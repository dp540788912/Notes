# String is awesome

## string in java is not iterable

To iterate a string, either use to ```toCharArray()``` or use ```get()``` method

```java
for(char c: str.toCharArray()){}
str.get(i)
```

## get char by index

```java
str.charAt(2)
```

## Find index of a matching substring

```java
str.indexOf(str2)
// return -1 if no substring matches str2, else return the index of the first element
```
