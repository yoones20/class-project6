import sqlite3
 
conn = sqlite3.connect("madrese.db")

corsur = conn.cursor()

corsur.execute ('''
            CREAT TABLE IF NOT EXIST madrese
            id INTEGER PRIMERY KEY
            name TEXT NOT NUL
            age INTEGER   
''')
