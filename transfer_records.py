import os

import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")

django.setup()


import pandas as pd

import pyodbc

import sqlite3

from django.conf import settings




# Set up Postgres connection

cnxn = pyodbc.connect(

#     "DRIVER=;"

#     "SERVER=;"

#     "DATABASE=;"

#     "UID=;"

#     "PWD=;"

)




# Set up SQLite3 connection

sqlite3_conn = sqlite3.connect("db.sqlite3")




# List of tables to transfer

table_names = [

#List table names here

]




# Iterate over table names and transfer records

for table_name in table_names:
    query = f"SELECT * FROM {table_name}"
    df = pd.read_sql(query, cnxn)
    df.to_sql(table_name, sqlite3_conn, if_exists="replace", index=False)




# Close connections

cnxn.close()

sqlite3_conn.close()


