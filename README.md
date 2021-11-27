# Online-Academy


This project is for inserting data to AWS Postgres Database (version 12.8),
and generating random transaction data.

_Note: For successfully running the scripts 
you must have a Postgres database with its credentials._ 

In order to connect to database and execute commands, 
you have to create a `database.ini` file in the `config` directory
with the following content:

```
[postgresql]
host=Your host
database=Your database name
user=Your username
password=Your password
```

##Main data insertion

Data insertion consists of several stages.
Main insert scripts are in insert directory. 
In order to successfully insert
random data run the scripts in following order:

1. init_tables.py
2. static_insert.py
3. fake_insert.py
4. csv_insert.py

_Note: You can change the content in `txt` files
in `recourse` directory with your specific data._

## Transactional data insertion

After the main data is inserted you can run generators
located in `generator` directory to generate and insert data into
transactional tables.