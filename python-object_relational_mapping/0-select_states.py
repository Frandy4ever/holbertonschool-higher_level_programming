#!/usr/bin/python3

import sys
import MySQLdb


def list_states_with_names_starting_with_n(mysql_username, mysql_password, database_name):
  """Lists all states with a name starting with N (upper N) from the database.

  Args:
    mysql_username: The MySQL username.
    mysql_password: The MySQL password.
    database_name: The MySQL database name.

  Returns:
    A list of all states with a name starting with N (upper N).
  """

  # Connect to the MySQL server.
  db = MySQLdb.connect(host='localhost', port=3306, user=mysql_username, passwd=mysql_password, db=database_name)

  # Create a cursor object.
  cursor = db.cursor()

  # Execute the SQL query to list all states with a name starting with N.
  cursor.execute('SELECT name FROM states WHERE name LIKE \'N%\' ORDER BY id ASC')

  # Fetch all the rows from the cursor.
  states = cursor.fetchall()

  # Close the cursor and the database connection.
  cursor.close()
  db.close()

  return states

# Display the results.
states = list_states_with_names_starting_with_n('root', 'password', 'hbtn_0e_0_usa')
for state in states:
  print(state[0])
