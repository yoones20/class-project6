import sqlite3
 
conn = sqlite3.connect("madrese.db")

corsur = conn.cursor()

corsur.execute('''
CREATE TABLE IF NOT EXISTS madrese(
            id INTEGER PRIMARY KEY,
            fname TEXT,
            lname TEXT,
            age INTEGER,
            nubmer class INT,
            name teacher TXT, 
)
''')


more_users = ("1", "MAMMAD", "AKBARI", "20", "102", "MALEKI"),("2", "ali", "alian", "23", "maleki")
corsur.executemany("INSERT INTO users values(?, ?, ?, ?, ?, ?);", more_users)

corsur.execute("SELECT * FROM users")
one_result = corsur.fetchone()
print(one_result)
conn.commit()
conn.close

