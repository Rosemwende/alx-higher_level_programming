#!/usr/bin/python3
""" write a script that takes in arguments and
displays all values in the states table of
hbtn_0e_0_usa where name matches the argument
"""
import MySQLdb
import sys

def main():

    mysql_user = sys.argv[1]
    mysql_password = sys.argv[2]
    db_name = sys.argv[3]
    state_name = sys.argv[4]

    db = MySQLdb.connect(
            host="localhost",
            user=mysql_user,
            passwd=mysql_password,
            db=db_name,
            port=3306
            )


    cursor = db.cursor()

    query = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"
    cursor.execute(query, (state_name,))


    rows = cursor.fetchall()


    for row in rows:
        print(row)


        cursor.close()
        db.close()

        if __name__ == "__main__":
            main()
