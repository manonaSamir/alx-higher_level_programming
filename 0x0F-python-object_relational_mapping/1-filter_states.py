#!/usr/bin/python3

""" lists all states with a name starting with N from hbtn_0e_0_usa """

import MySQLdb
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    db = MySQLdb.connect(host="localhost", port=3306, user=username,
                         password=password, database=db_name, charset="utf8")
    result = db.cursor()
    result.execute("""SELECT * FROM states WHERE name
                LIKE 'N%' ORDER BY states.id""")
    rows = result.fetchall()
    for row in rows:
        print(row)
    result.close()
