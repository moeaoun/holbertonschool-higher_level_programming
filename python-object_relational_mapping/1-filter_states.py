#!/usr/bin/python3
"""Lists all states with a name starting with 'N' from the database."""

import MySQLdb
import sys

if __name__ == "__main__":
    # Retrieve command-line arguments
    username, password, db_name = sys.argv[1:4]

    # Connect to the database
    db = MySQLdb.connect(host="localhost", port=3306,
                         user=username, passwd=password, db=db_name)

    # Create a cursor object
    cur = db.cursor()

    # Execute the query to fetch states starting with 'N'
    cur.execute("SELECT * FROM states WHERE name LIKE BINARY 'N%' ORDER BY id ASC")

    # Fetch and print results
    for row in cur.fetchall():
        print(row)

    # Clean up
    cur.close()
    db.close()

