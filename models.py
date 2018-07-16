import sqlite3 as sql

def insertUser(url, name, address):
    con = sql.connect("database.db")
    cur = con.cursor()
    cur.execute("INSERT INTO records (url, name, address) VALUES (?,?,?)",(url, name , address))
    con.commit()
    con.close()

def retrieveUsers():
	con = sql.connect("database.db")
	cur = con.cursor()
	cur.execute("SELECT * FROM records")
	records = cur.fetchall()
	con.close()
	return records