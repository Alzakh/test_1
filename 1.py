import psycopg2

#from psycopg2.extras import DictCursor
from contextlib import closing
with closing(psycopg2.connect(dbname='test_db', user='postgres', password='123', host='localhost')) as conn:
    with conn.cursor() as cursor:
        cursor.execute('SELECT * FROM client LIMIT 5')
        for row in cursor:
            print(row)

conn = psycopg2.connect(dbname='test_db', user='postgres', password='123', host='localhost')
cursor = conn.cursor()

cursor.execute('SELECT * FROM client LIMIT 10')
records = cursor.fetchall()
