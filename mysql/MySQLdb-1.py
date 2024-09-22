import MySQLdb

db = MySQLdb.connect("127.0.0.1", "root", "", "mydb")
cur = db.cursor()
cur.execute("SELECT * from t1")
