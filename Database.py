import sqlite3
 
conn = sqlite3.connect("madrese.db")

corsur = conn.cursor()

corsur.execute ('''
            CREAT TABLE IF NOT EXIST users
            id INTEGER PRIMERY KEY
            fname TEXT
            lname TEXT 
            age INTEGER
            nubmer class INT
            name teacher TXT  
''')


more_users = ("1", "MAMMAD", "AKBARI", "20", "102", "MALEKI")
corsur.executemany("INSERT INTO users values(?, ?, ?, ?, ?, ?);", more_users)


conn.commit()

