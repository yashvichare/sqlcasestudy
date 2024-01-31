
import pandas as pd 
import numpy as np
import psycopg2
from sqlalchemy import create_engine

conn_string = 'postgresql://postgres:rootuser@localhost/painting'
db = create_engine(conn_string)
conn = db.connect()

files = ['artist', 'canvas_size', 'image_link', 'museum_hours', 'museum', 'product_size', 'subject', 'work']

for file in files:
    df = pd.read_csv(f'/Users/yashvichare/Downloads/sqlcasestudy/famous paintings/{file}.csv')
    df.to_sql(file, con=conn, if_exists='replace', index=False)
