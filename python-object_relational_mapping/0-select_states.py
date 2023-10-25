#!/usr/bin/python3
import sys
import MySQLdb

if __name__ == "__main__":
    # Check that the correct number of command-line arguments is provided.
    if len(sys.argv) != 4:
        print("Usage: python script.py <username> <password> <database_name>")
        sys.exit(1)

    # Extract the command-line arguments.
    username = sys.argv[1]
    password = sys.argv[2]
    database_name = sys.argv[3]

    # Connect to the MySQL server running on localhost at port 3306.
    db = MySQLdb.connect(host="localhost", port=3306, user=username, passwd=password, db=database_name)

    # Create a cursor.
    cursor = db.cursor()

    # Execute the SQL query to fetch states with names starting with 'N'.
    cursor.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id")

    # Fetch and display the results.
    results = cursor.fetchall()
    for row in results:
        print(row)

    # Close the cursor and the database connection.
    cursor.close()
    db.close()
