import sqlite3
conn = sqlite3.connect('db.sqlite3')
c = conn.cursor()
# c.execute("SELECT * FROM auctionitem")
x = c.fetchall()
print(x)
