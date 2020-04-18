import sqlite3

conn = sqlite3.connect(":memory:")

cur = conn.cursor()

cur.execute("""CREATE TABLE users 
                (user_id int, user_name varchar(255), 
                PRIMARY KEY (user_id));""")

cur.execute("INSERT INTO users VALUES (?, ?)", (245, "Alice"))
conn.commit()

cur.execute('SELECT * FROM users')
print(cur.fetchone())

conn.close()
