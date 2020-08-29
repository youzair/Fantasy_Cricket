'''import sqlite3
conn=sqlite3.connect('fantasy.db')
cur=conn.cursor()
cur.execute("select * from match where player='Rohit';")
rs=cur.fetchone()
print(rs[7])'''
s="hello"
print(s.replace("e","t"))
