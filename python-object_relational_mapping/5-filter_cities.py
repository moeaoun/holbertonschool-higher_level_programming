#!/usr/bin/python3
"""
Lists all cities of a given state from the database hbtn_0e_4_usa.
Usage: ./5-filter_cities.py <mysql_username> <mysql_password> <database_name> <state_name>
"""

import MySQLdb
import sys

if __name__ == "__main__":
    # Extract command-line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    state_name = sys.argv[4]

    # Connect to the MySQL database
    db = MySQLdb.connect(host="localhost", port=3306,
                         user=username, passwd=password, db=db_name)

    # Create cursor
    cur = db.cursor()

    # Execute SQL query with parameterized input to prevent SQL injection
    query = """
        SELECT cities.name
        FROM cities
        JOIN states ON cities.state_id = states.id
        WHERE states.name = %s
        ORDER BY cities.id ASC
    """
    cur.execute(query, (state_name,))

    # Fetch results and print city names
    cities = cur.fetchall()
    print(", ".join(city[0] for city in cities))

    # Close cursor and connection
    cur.close()
    db.close()

