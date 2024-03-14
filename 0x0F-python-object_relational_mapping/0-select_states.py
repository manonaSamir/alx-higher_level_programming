#!/usr/bin/python3

"""a script that lists all states from the database hbtn_0e_0_usa"""

from MySQLdb import _mysql
import sys

if __name__ == "__main__":
    db =_mysql.connect()
    args = sys.argv
    username = args[1]
    password = args[2]
    db_name = args[3]
    db =_mysql.connect(host="localhost", port=3306, user=username, password=password, db=db_name, charset="utf8")
    db.query("""SELECT * FROM states ORDER BY id""")
    rows = db.store_result()
    for row in rows:
        print(f"({row[0]}, '{row[1]}')")
