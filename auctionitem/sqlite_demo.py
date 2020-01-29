import sqlite3
conn = sqlite3.connect('auctionitem.db')
# conn = sqlite3.connect(':memory:')

c = conn.cursor()
# c.execute("INSERT INTO auctionitems VALUES ('First Piece', 'Mazzochi', 4000)")
c.execute("SELECT * FROM auctionitems")
x = c.fetchall()
print(x)

# c.execute("INSERT INTO auctionitems VALUES ('First Piece', 'Mazzochi', 4000)")
# c.execute("""CREATE TABLE auctionitems(
# 			title text,
# 			artist text
# 			price integer
# 			)""")

c.execute("""INSERT INTO auctionitems 
	          VALUES ('First Piece', 'Mazzochi')
	          """)

x = c.fetchall()
print(x)
conn.commit()
conn.close()

