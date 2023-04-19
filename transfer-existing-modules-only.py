import os

import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")

django.setup()

import pandas as pd

import pyodbc

import sqlite3

from django.conf import settings


# # Set up PostGres connection

cnxn = pyodbc.connect(
     'DRIVER='
     'SERVER='
     'DATABASE='
     'UID='
     'PWD='

)




# Set up SQLite3 connection

sqlite3_conn = sqlite3.connect('db.sqlite3')




# Get list of all table names in MSSQL database

query = "SELECT TABLE_NAME FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_TYPE = 'BASE TABLE' AND TABLE_CATALOG = 'RAMS'"

table_names = pd.read_sql(query, cnxn)['TABLE_NAME'].tolist()




# Get list of all models in SQLite3 database

query = "SELECT name FROM sqlite_master WHERE type='table'"

model_names = pd.read_sql(query, sqlite3_conn)['name'].tolist()




# Iterate over table names and transfer records for tables that have corresponding models in SQLite3 database

for table_name in table_names:
    if table_name in model_names:
        query = f"SELECT * FROM {table_name}"
        df = pd.read_sql(query, cnxn)
        df.to_sql(table_name, sqlite3_conn, if_exists='replace', index=False)




# Close connections

cnxn.close()

sqlite3_conn.close()
