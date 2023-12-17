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
                    SELECT cities.name
                    FROM cities
                    INNER JOIN states
                    ON states.id = cities.state_id
                    WHERE states.name = %s
                    ORDER BY cities.id;
    """, (argv[4],))

    cities = cursor.fetchall()

    print(", ".join(map(lambda city: city[0], cities)))

    cursor.close()
    conn.close()
