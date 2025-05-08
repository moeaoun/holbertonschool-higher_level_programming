#!/usr/bin/python3
"""
Lists all cities from the database hbtn_0e_4_usa with their state names.
Usage: ./4-cities_by_state.py <mysql_username> <mysql_password> <database_name>
"""

import MySQLdb
import sys

if __name__ == "__main__":
    # Command-line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    # Connect to MySQL database
    db = MySQLdb.connect(host="localhost", port=3306,
                         user=username, passwd=password, db=db_name)

    # Create cursor
    cur = db.cursor()

    # SQL query to get cities and their corresponding states
    query = """
        SELECT cities.id, cities.name, states.name
        FROM cities
        JOIN states ON cities.state_id = states.id
        ORDER BY cities.id ASC
    """
    cur.execute(query)

    # Print each result
    for row in cur.fetchall():
        print(row)

    # Close cursor and connection
    cur.close()
    db.close()
