#!/usr/bin/python3
"""list all the states in the database"""
import sys

import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(
        host="localhost",
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3],
        port=3306,
    )
    cur = db.cursor()
    cur.execute("SELECT * FROM states")
    r = cur.fetchall()
    for s in r:
        print(s)
    cur.close()
    db.close()
