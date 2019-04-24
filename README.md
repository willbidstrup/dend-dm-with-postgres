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


2019-04-10  
I created a studentdb with user = student and password = student on my local machine.  This improved the error I was getting when running create_tables - previously I was getting a connection error, now I am getting "psycopg2.ProgrammingError: can't execute an empty query"  

To run Postgres on my local machine I need to firstly cd to ~ and then run sudo -u postgres psql postgres. This gets me to the psql interface and from there I can follow along with tutorials such as https://www.codementor.io/engineerapart/getting-started-with-postgresql-on-mac-osx-are8jcopb   

Questions at the end of this day;  

- what query should I write for song_select in sql_queries.py? Is this where i can choose to put my own query or is there something specified?  
- what types of variables should the columns in tables be - check with SQL training  
- how can I access the data on my local machine? Not clear in project description, looks like it's available in the project workspace  
- how I can I test if my SQL queries work? How to test minimum steps?  

2019-04-11  

I ended up zipping the data direct from the project workspace so i have exactly the same data - easier than trying to re-create from source.  

I found an issue trying to restart the jupyter notebook on local machine and disconnect from sparkifydb - this was useful https://dba.stackexchange.com/questions/16426/how-to-drop-all-connections-to-a-specific-database-without-stopping-the-server  

Not able to run create_tables.py - error says "table songplays does not exist"  

**Main issue is - cannot seem to create empty tables**   

TODO for tomorrow...  

1. Resolve issue around creating blank tables with create_tables.py  *DONE!*
2. Test ETL script, must be able to bring in data and transform with SQL queries - revise python/SQL as needed
3. Set up the infrastructure so next week I can focus on the actual modeling!  


2019-04-12  

Fixed sql_queries.py by adding IF EXISTS to DROP statement  

Dealt with git issues :)  

Successfully checked all tables in test.ipynb BUT the 'time' table is not working. Will check by altering sql_queries.py  

Sucessfully opened and closed connection to sparkifydb with test.ipynb. Used "SELECT * FROM pg_stat_activity;" to  check connection status in psql  *kept this open in seperate terminal window*  

**Today I have completed the first part of the project;**
Create Tables  
Write CREATE statements in sql_queries.py to create each table.  
Write DROP statements in sql_queries.py to drop each table if it exists.  
Run create_tables.py to create your database and tables.  
Run test.ipynb to confirm the creation of your tables with the correct columns. Make sure to click "Restart kernel" to close the connection to the database after running this notebook.  


TODO for Monday...

1. Figure out correct column types for each variable in each table and alter SQL queries accordingly.   

2019-04-15  

Today I need to;  

- get ETL jupyter notebook working  *DONE with minimal example #1 and # 2*  

Check this https://medium.com/dunder-data/selecting-subsets-of-data-in-pandas-6fcd0170be9c 

- get etl.py working  



Tomorrow I need to;  

- adjust everything including naming of Primary keys etc to create the actual schema  
- complete documentation  and submit  



2019-04-16  

The project is due today and I will struggle to complete.  

Taking juch longer to do the ETL than I thought.  

This works to disconnect sparkifydb in case of notebook hanging ...  select pg_terminate_backend(pid) from pg_stat_activity where datname='sparkifydb'



2019-04-23

Today I am back in the game. I've set up the project on my work computer so I can study remotely and also set up a new branch (workdev) so I don't screw anything up that already works!

To set up my work computer I needed to;

- install postgres with homebrew then create student user and studentdb database
- install pycorpg2 and ipython-sql via anaconda
- git clone my repo and start a new branch
- download the data from project session by opening terminal and zip -r data.zip data

** Now I can work on my remote computer!!**

2019-04-24

Today I am going to attempt to create the ETL script.

First I am going to use exactly whta I have in the notebook and in doing so uncover any errors. I have a feeling there are some instances where I am not selecting only one row.

I am getting this error;

30 files found in data/log_data
Traceback (most recent call last):
File "etl_dev.py", line 91, in <module>
main()
File "etl_dev.py", line 85, in main
process_data(cur, conn, filepath='data/log_data', func=process_log_file)
File "etl_dev.py", line 75, in process_data
func(cur, datafile)
File "etl_dev.py", line 57, in process_log_file
songplay_data = (row.ts,row.userId,row.level,song_id,artist_id,row.sessionId,row.location,row.userAgent)
NameError: name 'song_id' is not defined


**TODO**  Find out how to export/import ERD from my database


I changed my sql queries to include primary keys and now i get this error;

Traceback (most recent call last):
File "etl_dev.py", line 91, in <module>
main()
File "etl_dev.py", line 84, in main
process_data(cur, conn, filepath='data/song_data', func=process_song_file)
File "etl_dev.py", line 75, in process_data
func(cur, datafile)
File "etl_dev.py", line 20, in process_song_file
cur.execute(artist_table_insert, artist_data)
psycopg2.IntegrityError: duplicate key value violates unique constraint "artists_pkey"
DETAIL:  Key (artist_id)=(ARNTLGG11E2835DDB9) already exists.







