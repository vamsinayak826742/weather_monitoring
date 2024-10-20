import sqlite3

def create_connection(db_file):
    conn = sqlite3.connect(db_file)
    return conn

def create_table(conn):
    sql_create_weather_table = """CREATE TABLE IF NOT EXISTS weather (
                                    id INTEGER PRIMARY KEY,
                                    city TEXT NOT NULL,
                                    date TEXT NOT NULL,
                                    avg_temp REAL,
                                    max_temp REAL,
                                    min_temp REAL,
                                    dominant_condition TEXT
                                );"""
    try:
        cursor = conn.cursor()
        cursor.execute(sql_create_weather_table)
    except Exception as e:
        print(f"Error creating table: {e}")

def insert_weather_summary(conn, summary):
    sql_insert = """INSERT INTO weather (city, date, avg_temp, max_temp, min_temp, dominant_condition)
                    VALUES (?, ?, ?, ?, ?, ?);"""
    try:
        cursor = conn.cursor()
        cursor.execute(sql_insert, summary)
        conn.commit()
    except Exception as e:
        print(f"Error inserting data: {e}")
