#!/usr/bin/python3
""" This script lists all states from the database hbtn_0e_0_usa """
import sys
import MySQLdb

if __name__ == "__main__":
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]
    
    try:
        conn = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=mysql_username,
            passwd=mysql_password,
            db=database_name,
            charset="utf8"
            )

    except MySQLdb.Error as e:
        print("Error connecting to database: {}".format(e))
        sys.exit(1)

        cur = conn.cursor()
        cursor.execute("SELECT * FROM states ORDER BY id ASC")
        rows = cursor.fetchall()

    for row in rows:
        print(row)

        cursor.close()
        conn.close()
