import sqlite3
 
conn = sqlite3.connect("madrese.db")

corsur = conn.cursor()

corsur.execute ('''
            CREAT TABLE IF NOT EXIST madrese
            id INTEGER PRIMERY KEY
            fname TEXT
            lname TEXT 
            age INTEGER
            nubmer class INT
            name teacher TXT  
''')


corsur.execute('''INSERT INTO madrese(id, fname, lname, age, number class, name teacher''')
VALUES = ("1", "MAMMAD", "AKBARI", "20", "102", "MALEKI")

conn.commit()

