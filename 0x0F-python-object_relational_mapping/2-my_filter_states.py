#!/usr/bin/python3
"""a module that connects to a database and retrives data"""

import MySQLdb
import sys


def list_states(username, password, database_name, state_name_searched):
    """lists the states and gets the data"""
    try:
        db = MySQLdb.connect(
            host='localhost',
            user=username,
            port=3306,
            passwd=password,
            db=database_name
        )
        cursor = db.cursor()
    except MySQLdb.Error as e:
        print("Error: Unable to connect to MySQL server.")
        print("MySQL Error {}: {}".format(e.args[0], e.args[1]))
        return

    try:
        cursor.execute(
                "SELECT * "
                "FROM states "
                "WHERE name = {} "
                "ORDER BY id".format(state_name_searched)
                )

        results = cursor.fetchall()
        for row in results:
            print(row)

    finally:
        cursor.close()
        db.close()


if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: python script.py <mysql_username> <mysql_password> \
                <database_name> <state_name_searched>")
    else:
        username, password, database_name, state_name_searched = sys.argv[
            1], sys.argv[2], sys.argv[3], sys.argv[4]
        list_states(username, password, database_name, state_name_searched)
