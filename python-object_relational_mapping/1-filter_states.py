#!/usr/bin/python3
"""
Lists all states with a name starting with 'N'
from the database hbtn_0e_0_usa.
Usage: ./1-filter_states.py <mysql_username> <mysql_password> <database_name>
"""

import MySQLdb
import sys

if __name__ == "__main__":
    # Get command-line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    # Connect to the MySQL database
    db = MySQLdb.connect(host="localhost", port=3306,
                         user=username, passwd=password, db=db_name)

    # Create a cursor object to execute SQL queries
    cur = db.cursor()

    # Execute query to select states starting with 'N'
    cur.execute("SELECT * FROM states WHERE name LIKE BINARY 'N%' ORDER BY id ASC")

    # Fetch and print all matching rows
    for row in cur.fetchall():
        print(row)

    # Close the cursor and the database connection
    cur.close()
    db.close()

