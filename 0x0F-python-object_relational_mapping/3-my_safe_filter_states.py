#!/usr/bin/python3

"""
script takes in arguments and displays all values in
the states table of hbtn_0e_0_usa where name matches the argument.
But this time, write one that is safe from MySQL injections!
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
                    name = %s ORDER BY \
                    states.id ASC", (argv[4],))

    # Fetch all the rows
    states = cursor.fetchall()

    # Print the results
    for state in states:
        print(state)
