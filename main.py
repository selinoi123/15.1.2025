import sqlite3
import os

if os.path.exists("db.solution_hw,"):
    os.remove("db.solution_hw,")
    print("File removed successfully.")
else:
    print("The file does not exist.")


conn = sqlite3.connect("hw_solution.db,")
conn.row_factory = sqlite3.Row
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS shopping (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        amount INTEGER NOT NULL
    )
''')

cursor.execute("INSERT INTO shopping VALUES (1, 'Avokado', 5)")
cursor.execute("INSERT INTO shopping VALUES (2, 'Milk', 2)")
cursor.execute("INSERT INTO shopping VALUES (3, 'Bread', 3)")
cursor.execute("INSERT INTO shopping VALUES (4, 'Chocolate', 8)")
cursor.execute("INSERT INTO shopping VALUES (5, 'Bamba', 5)")
cursor.execute("INSERT INTO shopping VALUES (6, 'Orange', 10)")

conn.commit()

cursor.execute("SELECT * FROM shopping")
cursor.execute("SELECT * FROM shopping WHERE amount > 5")
cursor.execute("DELETE FROM shopping WHERE name LIKE 'Orange'")
cursor.execute("UPDATE shopping SET name = 'Bisli' WHERE name LIKE 'Bamba'")
cursor.execute("UPDATE shopping SET amount=1 WHERE name LIKE 'Milk'")
cursor.execute("SELECT COUNT(*) FROM shopping")
cursor.execute("SELECT * FROM shopping WHERE id > 0")

cursor.execute("SELECT * FROM shopping")
final_rows = cursor.fetchall()
for row in final_rows:
    print(dict(row))

conn.close()


