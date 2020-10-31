#!/usr/bin/env python3
"""
Main file
"""

get_db = __import__('filtered_logger').get_db

db = get_db()
cursor = db.cursor()
cursor.execute("SELECT COUNT(*) FROM users;")
for row in cursor:
    print(row[0])
cursor.close()
db.close()

# PERSONAL_DATA_DB_USERNAME=root PERSONAL_DATA_DB_PASSWORD=Java_1988 PERSONAL_DATA_DB_HOST=localhost PERSONAL_DATA_DB_NAME=my_db ./3-main.py
