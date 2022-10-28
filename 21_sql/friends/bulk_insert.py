import sqlite3

conn = sqlite3.connect("my_friends.db")
c = conn.cursor()

people = [
    ("Roald", "Amundsen", 5),
    ("Rosa", "Parks", 8),
    ("Henry", "Hudson", 7),
    ("Neil", "Armstrong", 7),
    ("Daniel", "Boone", 3),
]

c.executemany("INSERT INTO friends VALUES (?,?,?)", people)

conn.commit()
conn.close()
