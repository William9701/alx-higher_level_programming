#!/usr/bin/python3
"""a module that connects to a database and retrives data"""

import MySQLdb
import sys

def search_states(username, password, database_name, state_name):
    try:
        db = MySQLdb.connect(
            host='localhost',
            port=3306,
            user=username,
            passwd=password,
            db=database_name
        )
        cursor = db.cursor()

        # SQL query with a parameterized query
        sql_query = "SELECT * FROM states WHERE name = %s ORDER BY id"

        
        # Execute the SQL query with the state_name as a parameter
        cursor.execute(sql_query, (state_name,))

        # Fetch and display the results
        results = cursor.fetchall()
        for row in results:
            print("{}: {}".format(row[0], row[1]))

    except MySQLdb.Error as e:
        print("MySQL Error {}: {}".format(e.args[0], e.args[1]))
    finally:
        cursor.close()
        db.close()

if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: python script.py <mysql_username> <mysql_password> <database_name> <state_name>")
    else:
        username, password, database_name, state_name = sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]
        search_states(username, password, database_name, state_name)
