#!/usr/bin/python3
"""This module lists states"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    conn = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=argv[1],
        passwd=argv[2],
        db=argv[3],
        charset="utf8"
        )

    cursor = conn.cursor()

    cursor.execute("""SELECT * from states
                ORDER BY states.id;""")

    states = cursor.fetchall()

    for state in states:
        print(state)

    cursor.close()
    conn.close()
