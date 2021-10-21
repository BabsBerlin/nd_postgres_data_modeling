"""
SPARKIFY DB
This file contains all SQL queries to drop, create, and populate the db. 
It is accessed by 'create_tables.py' to drop and create the db and by 'etl.py' to populate the db from the JSON files.
"""



# DROP TABLES: sql queries to drop existing versions of the db tables to later create an empty, new version of it.

songplay_table_drop = "DROP TABLE IF EXISTS songplays;"
user_table_drop = "DROP TABLE IF EXISTS users;"
song_table_drop = "DROP TABLE IF EXISTS songs;"
artist_table_drop = "DROP TABLE IF EXISTS artists;"
time_table_drop = "DROP TABLE IF EXISTS time;"



# CREATE TABLES: sql queries to create all necessary tables for the Sparkify db

songplay_table_create = ("""
    CREATE TABLE IF NOT EXISTS songplays 
    (songplay_id SERIAL PRIMARY KEY, 
    start_time timestamp NOT NULL, 
    user_id int NOT NULL, 
    level varchar, 
    song_id varchar, 
    artist_id varchar, 
    session_id int, 
    location varchar, 
    user_agent varchar);
""")

user_table_create = ("""
    CREATE TABLE IF NOT EXISTS users 
    (user_id int PRIMARY KEY, 
    first_name varchar NOT NULL, 
    last_name varchar NOT NULL, 
    gender varchar, 
    level varchar);
""")

song_table_create = ("""
    CREATE TABLE IF NOT EXISTS songs 
    (song_id varchar PRIMARY KEY, 
    title varchar NOT NULL, 
    artist_id varchar, 
    year int, 
    duration numeric);
""")

artist_table_create = ("""
    CREATE TABLE IF NOT EXISTS artists 
    (artist_id varchar PRIMARY KEY, 
    name varchar NOT NULL, 
    location varchar, 
    latitude numeric, 
    longitude numeric);
""")

time_table_create = ("""
    CREATE TABLE IF NOT EXISTS time
    (start_time timestamp PRIMARY KEY, 
    hour int, 
    day int, 
    week int, 
    month int, 
    year int, 
    weekday int);
""")



# INSERT RECORDS: sql queries to insert data into the tables

songplay_table_insert = ("""
    INSERT INTO songplays (start_time, user_id, level, song_id, artist_id, session_id, location, user_agent)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s);
""")

user_table_insert = ("""
    INSERT INTO users (user_id, first_name, last_name, gender, level)
    VALUES (%s, %s, %s, %s, %s)
    ON CONFLICT (user_id) DO UPDATE
    SET level = EXCLUDED.level;
""")

song_table_insert = ("""
    INSERT INTO songs (song_id, title, artist_id, year, duration)
    VALUES (%s, %s, %s, %s, %s)
    ON CONFLICT (song_id) DO NOTHING;
""")

artist_table_insert = ("""
    INSERT INTO artists (artist_id, name, location, latitude, longitude)
    VALUES (%s, %s, %s, %s, %s)
    ON CONFLICT (artist_id) DO NOTHING;
""")


time_table_insert = ("""
    INSERT INTO time (start_time, hour, day, week, month, year, weekday)
    VALUES (%s, %s, %s, %s, %s, %s, %s)
    ON CONFLICT (start_time) DO NOTHING;
""")



# FIND SONGS: sql query to find the song ID and artist ID based on the title, artist name, and duration of a song; used to populate the songplays table

song_select = ("""
    SELECT s.song_id, a.artist_id FROM songs AS s INNER JOIN artists AS a ON s.artist_id = a.artist_id
    WHERE s.title = %s AND a.name = %s AND round(s.duration,3) = %s;
""")



# QUERY LISTS: combine sql queries into lists for easy import into create_tables.py

create_table_queries = [songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]