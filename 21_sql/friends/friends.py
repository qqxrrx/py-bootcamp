import sqlite3

conn = sqlite3.connect("my_friends.db")
# create cursor object
c = conn.cursor()
# execute some sql

# c.execute(
#     "CREATE TABLE friends (first_name TEXT, last_name TEXT, closeness INTEGER);")

# insert_query = """INSERT INTO friends
#                   VALUES ('Merriwether', 'Lewis', 7)"""
# c.execute(insert_query)

form_first = 'john'
# sanitize using ? to avoid sql injection
query = f"INSERT INTO friends (first_name) VALUES (?)"
# pass tuple
c.execute(query, (form_first, ))

data = ("maria", "renard", 10)
query = f"INSERT INTO friends VALUES (?,?,?)"
c.execute(query, data)

# commit changes
conn.commit()
conn.close()
