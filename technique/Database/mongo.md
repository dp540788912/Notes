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