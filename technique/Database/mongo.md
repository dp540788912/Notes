# about mong 

## Dump a database and restore in another mongodb address

- dump 
```
mongodump -h 192.168.10.30 -u root -p root --port 27017 --authenticationDatabase admin -d bond -c bond_sector -o ./bond_d_bak.ba
// -h host
// -u user 
// -p password
// --port port 
// -d database 
// -c collection 
```

- restore 

```
mongorestore -h 192.168.10.30 -u root -p root --port 27017 --authenticationDatabase admin -d bond -c bond_sector ./bond_d_bak.ba

```


## basic  operation 

in mongo db, if attr is an array, "equal" is techniqully "in"
```
mongo.db.find("items": "value")
```

if "items" is an array, this means "value" in "items"

## easily confused operation 

- $pull

delete items in an array 

- $unset 

delete fields, or attributes 


## connect mongo db 
```
mongo 192.168.10.14:27017 --username root --password Ricemap123 --authenticationDatabase admin
```
watch this --authenticationDatabase admin, there will be error if neglected 



# language support 
## pymongo delete items and count 

```python
result = client.db.col.delete_many({"_id": "aas"})
print(result.delete_count)
```