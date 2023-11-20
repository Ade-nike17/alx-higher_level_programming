#!/usr/bin/python3

"""
This script that takes in an argument and displays all
values in the states table of hbtn_0e_0_usa where name
matches the argument.
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    # Connect to MySQL server
    db = MySQLdb.connect(host="localhost", port=3306,
                         user=argv[1], passwd=argv[2], db=argv[3])
    cursor = db.cursor()

    # Execute the SQL query to fetch states
    cursor.execute("SELECT * FROM states WHERE \
                    name LIKE BINARY '{}' ORDER BY \
                    states.id ASC".format(argv[4]))

    # Fetch all the rows
    states = cursor.fetchall()

    # Print the results
    for state in states:
        print(state)
