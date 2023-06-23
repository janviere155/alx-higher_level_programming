#!/usr/bin/python3
"""Filter all the states in the database based on the specified condition"""
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
    cur.execute(
        """SELECT * FROM states WHERE name
        LIKE %s ORDER BY states.id""",
        (sys.argv[4],),
    )
    r = cur.fetchall()
    for s in r:
        print(s)
    cur.close()
    db.close()
