#!/usr/bin/python3

"""
This script that lists all cities from the database hbtn_0e_4_usa.
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    # Connect to MySQL server
    db = MySQLdb.connect(host="localhost", port=3306,
                         user=argv[1], passwd=argv[2], db=argv[3])
    cursor = db.cursor()

    # Execute the SQL query to fetch cities
    cursor.execute("""
           SELECT
               cities.id, cities.name, states.name
           FROM
               cities
           JOIN
               states
           ON
               cities.state_id = states.id
           ORDER BY
               cities.id ASC
    """)

    # Fetch all the rows
    cities = cursor.fetchall()

    # Print the results
    for city in cities:
        print(city)
