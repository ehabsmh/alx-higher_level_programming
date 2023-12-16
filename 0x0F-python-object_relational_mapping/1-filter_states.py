#!/usr/bin/python3
"""lists all states with a name starting with N"""


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

    filtered_states = cursor.fetchall()

    for state in filtered_states:
        if state[1].startswith("N"):
            print(state)

    cursor.close()
    conn.close()
