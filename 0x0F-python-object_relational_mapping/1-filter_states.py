#!/usr/bin/python3
"""a module that connects to a database and retrives data """

import MySQLdb
import sys


def list_states(username, password, database_name):
    """lists the states"""
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
        cursor.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id")
        results = cursor.fetchall()
        for row in results:
            print(row)
    except MySQLdb.Error as e:
        print("MySQL Error {}: {}".format(e.args[0], e.args[1]))
    finally:
        cursor.close()
        db.close()


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python script.py <mysql_username> \
                <mysql_password> <database_name>")
    else:
        username, password, database_name = sys.argv[1], \
                sys.argv[2], sys.argv[3]
        list_states(username, password, database_name)
