#!/usr/bin/python3

"""
This script takes in the name of a state as an argument
lists all cities of that state,
using the database hbtn_0e_4_usa
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
               cities.id, cities.name
           FROM
               cities
           JOIN
               states
           ON
               cities.state_id = states.id
           WHERE
               states.name LIKE BINARY %(state_name)s
           ORDER BY
               cities.id ASC
    """, {'state_name': argv[4]})

    # Fetch all the rows
    cities = cursor.fetchall()

    # Print the results
    if cities is not None:
        print(", ".join([city[1] for city in cities]))
