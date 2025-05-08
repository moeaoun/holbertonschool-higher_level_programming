#!/usr/bin/python3
"""
Lists all values in the states table of hbtn_0e_0_usa
where name matches the user input (argument), using format() for the query.
Usage: ./2-my_filter_states.py <username> <password> <database_name> <state_name>
"""

import MySQLdb
import sys

if __name__ == "__main__":
    # Get input arguments
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    state_name = sys.argv[4]

    # Connect to database
    db = MySQLdb.connect(host="localhost", port=3306,
                         user=username, passwd=password, db=db_name)

    # Create cursor
    cur = db.cursor()

    # Create query using format (NOTE: vulnerable to SQL injection by design for this task)
    query = "SELECT * FROM states WHERE name LIKE BINARY '{}' ORDER BY id ASC".format(state_name)

    # Execute query
    cur.execute(query)

    # Print results
    for row in cur.fetchall():
        print(row)

    # Close connection
    cur.close()
    db.close()

