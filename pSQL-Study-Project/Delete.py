import psycopg2
from psycopg2 import Error
import password


def create_db_connection(user_name, user_password, host_address, server_port, db_name):
    connection = None
    try:
        connection = psycopg2.connect(user=user_name,
                                      password=user_password,
                                      host=host_address,
                                      port=server_port,
                                      database=db_name
                                      )
        print("PostgreSQL Database connection successful")
    except Error as err:
        print(f"Error: '{err}'")

    return connection


def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query successful")
    except Error as err:
        print(f"Error: '{err}'")


def read_query(connection, query):
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as err:
        print(f"Error: '{err}'")


connection = create_db_connection(user_name="postgres",
                                  user_password=password.user_password,
                                  host_address="127.0.0.1",
                                  server_port="5432",
                                  db_name="school")


# delete a record from table
delete_course = """
DELETE FROM course 
WHERE course_id = 20;
"""
execute_query(connection, delete_course)


# remove a column from table
delete_column = """
ALTER TABLE client
DROP COLUMN industry;
"""
execute_query(connection, delete_column)


# drops table
drop_table = """
DROP TABLE takes_course
"""
execute_query(connection, drop_table)

# drops the rest of schemas
drop_rest = """
DROP TABLE course;
DROP TABLE participant;
DROP TABLE client;
DROP TABLE teacher;
"""
execute_query(connection, drop_rest)