#!/usr/bin/python3
"""Lists all cities"""

from sys import argv
import MySQLdb


if __name__ == "__main__":
    conn = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=argv[1],
            passwd=argv[2],
            db=argv[3]
            )

    cursor = conn.cursor()

    cursor.execute("""
                    SELECT cities.id, cities.name, states.name
                    FROM cities
                    INNER JOIN states
                    ON cities.state_id = states.id
                    ORDER BY cities.id;
    """)

    cities = cursor.fetchall()

    for city in cities:
        print(city)

    cursor.close()
    conn.close()
