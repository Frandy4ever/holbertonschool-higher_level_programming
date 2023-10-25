#!/usr/bin/python3
""" script that takes in an argument and displays all values
in the states table of hbtn_0e_0_usa where name matches the argument."""
import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )

    cursor = db.cursor()

    state_name = sys.argv[4]

    query = "SELECT * FROM states WHERE name = '{}' " \
            "ORDER BY id ASC".format(state_name)
    cursor.execute(query)

    result_states = cursor.fetchall()

    for state in result_states:
        print(state)

    cursor.close()
    db.close()
