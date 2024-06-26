#!/usr/bin/python3
""" Write a script that lists all cities from the database hbtn_0e_4_usa """
import MySQLdb
import sys

def main():

    mysql_user = sys.argv[1]
    mysql_password = sys.argv[2]
    db_name = sys.argv[3]


    db = MySQLdb.connect(
            host="localhost",
            user=mysql_user,
            passwd=mysql_password,
            db=db_name,
            port=3306
            )


    cursor = db.cursor()


    query = """
    SELECT cities.id, cities.name, states.name
    FROM cities
    JOIN states ON cities.state_id = states.id
    ORDER BY cities.id ASC
    """

    cursor.execute(query)


    rows = cursor.fetchall()


    for row in rows:
        print(row)


        cursor.close()
        db.close()

        if __name__ == "__main__":
            main()
