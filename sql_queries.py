# DROP TABLES

songplay_table_drop = "DROP TABLE IF EXISTS songplays"
user_table_drop = "DROP TABLE IF EXISTS  users"
song_table_drop = "DROP TABLE IF EXISTS  songs"
artist_table_drop = "DROP TABLE IF EXISTS  artists"
time_table_drop = "DROP TABLE IF EXISTS  time"

# CREATE TABLES

user_table_create = ("""CREATE TABLE IF NOT EXISTS users (user_id int PRIMARY KEY,
first_name varchar, last_name varchar, gender varchar, level varchar);
""")

song_table_create = ("""CREATE TABLE IF NOT EXISTS songs (song_id varchar PRIMARY KEY,
title varchar, artist_id varchar, year int, duration int);
""")

artist_table_create = ("""CREATE TABLE IF NOT EXISTS artists (artist_id varchar PRIMARY KEY,
artist_name varchar, artist_location varchar, artist_latitude varchar, artist_longitude varchar);
""")

time_table_create = ("""CREATE TABLE IF NOT EXISTS time (start_time time without time zone PRIMARY KEY,
hour int, day int, week int, month int, year int, weekday int);
""")

songplay_table_create = ("""CREATE TABLE IF NOT EXISTS songplays (songplay_id SERIAL PRIMARY KEY,
start_time time without time zone NOT NULL, user_id int NOT NULL, level varchar, song_id varchar, artist_id varchar,
session_id int, location varchar, user_agent varchar,
FOREIGN KEY (start_time) REFERENCES time(start_time),
FOREIGN KEY (user_id) REFERENCES users(user_id),
FOREIGN KEY (song_id) REFERENCES songs(song_id),
FOREIGN KEY (artist_id) REFERENCES artists(artist_id));
""")

# INSERT RECORDS

user_table_insert = ("""INSERT INTO users (user_id, first_name, last_name,
gender, level) \
                 VALUES (%s, %s, %s, %s, %s)
                 ON CONFLICT (user_id) DO NOTHING;
""")

song_table_insert = ("""INSERT INTO songs (song_id, title, artist_id,
year, duration) \
                 VALUES (%s, %s, %s, %s, %s)
                 ON CONFLICT (song_id) DO NOTHING;
""")

artist_table_insert = ("""INSERT INTO artists (artist_id, artist_name, artist_location, artist_latitude,
artist_longitude) \
                 VALUES (%s, %s, %s, %s, %s)
                 ON CONFLICT (artist_id) DO NOTHING;
""")


time_table_insert = ("""INSERT INTO time (start_time, hour, day, week, month,
year, weekday) \
                 VALUES (%s, %s, %s, %s, %s, %s, %s)
                 ON CONFLICT (start_time) DO NOTHING;
""")

songplay_table_insert = ("""INSERT INTO songplays (start_time,
user_id, level, song_id, artist_id, session_id, location, user_agent) \
                 VALUES (%s, %s, %s, %s, %s, %s, %s, %s);
""")

# FIND SONGS

song_select = ("""SELECT s.song_id, a.artist_id FROM songs as s
LEFT JOIN artists as a
ON a.artist_id = s.artist_id
WHERE s.title = (%s) AND a.artist_name = (%s) AND s.duration=(%s)
""")

# QUERY LISTS

create_table_queries = [user_table_create, song_table_create, artist_table_create, time_table_create, songplay_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]
