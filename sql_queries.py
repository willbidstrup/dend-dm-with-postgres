# DROP TABLES

songplay_table_drop = "DROP table songplays"
user_table_drop = "DROP table users"
song_table_drop = "DROP table songs"
artist_table_drop = "DROP table artists"
time_table_drop = "DROP table timestamps"

# CREATE TABLES

songplay_table_create = ("""CREATE TABLE IF NOT EXISTS songplays (songplay_id int,
start_time int, user_id int, level varchar, song_id int, artist_id int,
session_id int, location var_char, user_agent varchar);
""")

user_table_create = ("""CREATE TABLE IF NOT EXISTS users (user_id int,
first_name varchar, last_name varchar, gender varchar, level varchar);
""")

song_table_create = ("""CREATE TABLE IF NOT EXISTS songs (song_id int,
title varchar, artist_id int, year int, duration int);
""")

artist_table_create = ("""CREATE TABLE IF NOT EXISTS artists (artist_id int,
name varchar, location varchar, latitude int, longitude int);
""")

time_table_create = ("""CREATE TABLE IF NOT EXISTS timestamps (start_time int,
hour int, day int, week int, month int, year int, weekday varchar);
""")

# INSERT RECORDS

songplay_table_insert = ("""INSERT INTO songplays (songplay_id, start_time,
user_id, level, song_id, artist_id) \
                 VALUES (%s, %s, %s, %s, %s, %s);
""")

user_table_insert = ("""INSERT INTO users (user_id, first_name, last_name,
gender, level) \
                 VALUES (%s, %s, %s, %s, %s);
""")

song_table_insert = ("""INSERT INTO songs (song_id, title, artist,
year, duration) \
                 VALUES (%s, %s, %s, %s, %s);
""")

artist_table_insert = ("""INSERT INTO songs (artist_id, name, location, latitude,
longitude) \
                 VALUES (%s, %s, %s, %s, %s);
""")


time_table_insert = ("""INSERT INTO timestamps (start_time, hour, day, week, month,
year, weekday) \
                 VALUES (%s, %s, %s, %s, %s, %s, %s);
""")

# FIND SONGS

song_select = ("""
""")

# QUERY LISTS

create_table_queries = [songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]
