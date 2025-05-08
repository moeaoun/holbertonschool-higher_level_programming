#!/usr/bin/python3
"""
Displays all values in the states table where name matches the argument.
Usage: ./2-my_filter_states.py <mysql_username> <mysql_password>
        <database_name> <state_name>
"""

import MySQLdb
import sys

if __name__ == "__main__":
    # Get command-line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    state_name = sys.argv[4]

    # Connect to the MySQL database
    db = MySQLdb.connect(host="localhost", port=3306,
                         user=username, passwd=password, db=db_name)

    # Create a cursor object to execute SQL queries
    cur = db.cursor()

    # Create the query with the user input using string formatting
    query = "SELECT * FROM states WHERE name = '{}' ORDER BY id ASC".format(state_name)
    cur.execute(query)

    # Fetch and print matching rows
    for row in cur.fetchall():
        print(row)

    # Close the cursor and database connection
    cur.close()
    db.close()
