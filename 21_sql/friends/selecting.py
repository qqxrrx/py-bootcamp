import sqlite3
conn = sqlite3.connect("my_friends.db")
c = conn.cursor()

c.execute("SELECT * FROM friends")

# for result in c: # iterator
#     print(result)

print(c.fetchall())  # return list

c.execute("SELECT * FROM friends WHERE first_name IS 'Rosa'")
print(c.fetchone())

c.execute("SELECT * FROM friends WHERE closeness > 5 ORDER BY closeness")
print(c.fetchall())

conn.commit()
conn.close()
