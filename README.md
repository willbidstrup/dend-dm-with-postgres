# Data Modeling with Postgres

## Executive Summary


## Database Schema and ETL Design



## Example Queries


#######################


## Approach

From the project description itself, these are the steps to be followed;  

- Create Tables  
- Build ETL Processes  
- Build ETL Pipeline  
- Document  



## File notes

### create_tables.py

### etl.ipynb

### etl.py  

### sql_queries.py  

### test.ipynb

## Learning notes


2018-04-10  
I created a studentdb with user = student and password = student on my local machine.  This improved the error I was getting when running create_tables - previously I was getting a connection error, now I am getting "psycopg2.ProgrammingError: can't execute an empty query"  

To run Postgres on my local machine I need to firstly cd to ~ and then run sudo -u psostrges psql psotgres. This gets me to the psql interface and from there I can follow along with tutorials such as https://www.codementor.io/engineerapart/getting-started-with-postgresql-on-mac-osx-are8jcopb   

Questions at the end of this day;  

- what query should I write for song_select in sql_queries.py? Is this where i can choose to put my own query or is there something specified?  
- what types of variables should the columns in tables be - check with SQL training  
- how can I access the data on my local machine? Not clear in project description, looks like it's available in the project workspace  
- how I can I test if my SQL queries work? How to test minimum steps?  

2018-04-11  

I ended up zipping the data direct from the project workspace so i have exactly the same data - easier than trying to re-create from source.  

I found an issue trying to restart the jupyter notebook on local machine and disconnect from sparkifydb - this was useful https://dba.stackexchange.com/questions/16426/how-to-drop-all-connections-to-a-specific-database-without-stopping-the-server  

Not able to run create_tables.py - error says "table songplays does not exist"  

**Main issue is - cannot seem to create empty tables**   

TODO for tomorrow...  

1. Resolve issue around creating blank tables with create_tables.py  
2. Test ETL script, must be able to bring in data and transform with SQL queries - revise python/SQL as needed
3. Set up the infrastructure so next week I can focus on the actual modeling!  
