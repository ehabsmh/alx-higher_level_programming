#!/usr/bin/python3
"""Displays all values in the states table where name matches the argument."""


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
                    WHERE states.name = '{}'
                    ORDER BY states.id;""".format(argv[4]))

    filtered_states = cursor.fetchall()

    for state in filtered_states:
        print(state)

    cursor.close()
    conn.close()
