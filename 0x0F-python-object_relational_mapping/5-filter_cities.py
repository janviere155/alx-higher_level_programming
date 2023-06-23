#!/usr/bin/python3
"""list all the cities in the database based on a certain state"""
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
        """SELECT cities.name
        FROM cities INNER JOIN states
        ON states.id=cities.state_id
        WHERE states.name=%s ORDER BY cities.id""",
        (sys.argv[4],),
    )
    r = cur.fetchall()
    tmp = list(s[0] for s in r)
    print(*tmp, sep=", ")
    cur.close()
    db.close()
