import sqlite3
conn = sqlite3.connect("users.db")


# warning: user can enter an SQL query if the query is not sanitized
u = input("username: ")  # enter: John
p = input("password: ")  # enter: ' OR 1=1--

c = conn.cursor()

# bad practice, use ? for the parameters!
# query = f"SELECT * FROM users WHERE username='{u}' AND password='{p}'"
# c.execute(query)

# best practice:
query = "SELECT * FROM users WHERE username=? AND password=?"
c.execute(query, (u, p,))

result = c.fetchone()

if (result):
    print(f"welcome back, {result}")
else:
    print("account does not exist or credentials wrong")

conn.commit()
conn.close()
