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


# Executing a few queries
q1 = """
SELECT *
FROM teacher;
"""
results = read_query(connection, q1)
print("SELECT * FROM teachers query result:")
for result in results:
    print(result)
print ("\n")

q2 = """
SELECT course.course_id, course.course_name, course.language, client.client_name, client.address
FROM course
JOIN client
ON course.client = client.client_id
WHERE course.in_school = FALSE;
"""

results = read_query(connection, q2)
print("Select courses not performed in school result:")
for result in results:
      print(result)
print ("\n")