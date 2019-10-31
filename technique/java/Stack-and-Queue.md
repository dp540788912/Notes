# Stack and Queue

## Stack

### operation

* add element

```java
Stack<String> str = new Stack<>();
str.push("this");
```

* get element

```java
str.pop();
```

## Queue

* reverse order

```java
Queue<String> pq = new PriorityQueue<>(26, Collections.reverseOrder())
```

* add elements

```java
pq.add("this")
```

* customized priority queue

```java
Queue<String> pq = new PriorityQueue<>(new Comparator<String>() {
            @Override
            public int compare(String o1, String o2) {
                return 0;
            }
        });
```

* check if empty

```java
pq.isEmpty()
```

* pop element

```java
pq.poll()
```
