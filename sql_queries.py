# DROP TABLES

songplay_table_drop = "DROP TABLE IF EXISTS songplays"
user_table_drop = "DROP TABLE IF EXISTS  users"
song_table_drop = "DROP TABLE IF EXISTS  songs"
artist_table_drop = "DROP TABLE IF EXISTS  artists"
time_table_drop = "DROP TABLE IF EXISTS  time"

# CREATE TABLES

songplay_table_create = ("""CREATE TABLE IF NOT EXISTS songplays (songplay_id int,
start_time int, user_id int, level varchar, song_id int, artist_id int,
session_id int, location varchar, user_agent varchar);
""")

user_table_create = ("""CREATE TABLE IF NOT EXISTS users (user_id varchar,
first_name varchar, last_name varchar, gender varchar, level varchar);
""")

song_table_create = ("""CREATE TABLE IF NOT EXISTS songs (song_id varchar,
title varchar, artist_id varchar, year int, duration int);
""")

artist_table_create = ("""CREATE TABLE IF NOT EXISTS artists (artist_id varchar,
artist_name varchar, artist_location varchar, artist_latitude varchar, artist_longitude varchar);
""")

time_table_create = ("""CREATE TABLE IF NOT EXISTS time (start_time time,
hour int, day int, week int, month int, year int, weekday int);
""") # Select better column types!!!!

# INSERT RECORDS

songplay_table_insert = ("""INSERT INTO songplays (songplay_id, start_time,
user_id, level, song_id, artist_id) \
                 VALUES (%s, %s, %s, %s, %s, %s);
""")

user_table_insert = ("""INSERT INTO users (user_id, first_name, last_name,
gender, level) \
                 VALUES (%s, %s, %s, %s, %s);
""")

song_table_insert = ("""INSERT INTO songs (song_id, title, artist_id,
year, duration) \
                 VALUES (%s, %s, %s, %s, %s);
""")

artist_table_insert = ("""INSERT INTO artists (artist_id, artist_name, artist_location, artist_latitude,
artist_longitude) \
                 VALUES (%s, %s, %s, %s, %s);
""")


time_table_insert = ("""INSERT INTO time (start_time, hour, day, week, month,
year, weekday) \
                 VALUES (%s, %s, %s, %s, %s, %s, %s);
""")

# FIND SONGS

song_select = ("""SELECT s.song_id, a.artist_id FROM songs as s
LEFT JOIN artists as a
ON a.artist_id = s.artist_id
WHERE s.title = (%s) AND a.artist_name = (%s) AND s.duration=(%s)
""")

# QUERY LISTS

create_table_queries = [songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]
