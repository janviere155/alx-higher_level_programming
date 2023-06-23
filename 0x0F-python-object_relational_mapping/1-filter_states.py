#!/usr/bin/python3
"""Filter all the states in the database that start with `N`"""
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
                LIKE BINARY 'N%' ORDER BY states.id"""
    )
    r = cur.fetchall()
    for s in r:
        print(s)
    cur.close()
    db.close()
