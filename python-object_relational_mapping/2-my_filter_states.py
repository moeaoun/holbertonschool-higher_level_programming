#!/usr/bin/python3
"""
Displays all values in the states table where name matches the argument.
Uses string formatting (not safe, per task requirements).
"""

import MySQLdb
import sys

if __name__ == "__main__":
    # Get command-line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    state_name = sys.argv[4]

    # Connect to the MySQL server
    db = MySQLdb.connect(host="localhost", port=3306,
                         user=username, passwd=password, db=db_name)

    # Create cursor and execute the query using string formatting
    cur = db.cursor()
    query = "SELECT * FROM states WHERE name LIKE BINARY '{}' ORDER BY id ASC".format(state_name)
    cur.execute(query)

    # Print the results
    for row in cur.fetchall():
        print(row)

    # Clean up
    cur.close()
    db.close()

