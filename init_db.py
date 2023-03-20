import sqlite3
# create a connection to a db
# execute the schema script: executescript() : executes multiple sql statements at once
connection = sqlite3.connect("database.db")
with open('schema.sql') as a:
    connection.executescript(a.read())
# set cursor object to be able to navigate rows in table created
# cursor object allows use to process rows in databases
cursor = connection.cursor()
# create dummy content
cursor.execute("INSERT INTO shoes (name, image, price) VALUES (?, ?,?)", ("Prada", "https://images.app.goo.gl/MRbUpGPGnk3ya83D9", "ksh10000"))
cursor.execute("INSERT INTO shoes (name,image, price) VALUES (?, ?, ?)", ('Toughees', "https://images.app.goo.gl/QXpuchEErRWKg4So7", "Ksh2500"))

connection.commit()
# close
connection.close()