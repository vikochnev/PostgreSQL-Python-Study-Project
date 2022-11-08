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


# reusable function to execute queries
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

# sample update query:
print("Entry before update:")
q1 = """
SELECT * 
FROM client
WHERE client_id = 101;
"""
results = read_query(connection, q1)
for result in results:
    print(result)

update = """
UPDATE client 
SET address = '23 Fingiertweg, 14534 Berlin' 
WHERE client_id = 101;
"""
execute_query(connection, update)

print("Entry after update:")
q2 = """
SELECT * 
FROM client
WHERE client_id = 101;
"""
results = read_query(connection, q2)
for result in results:
    print(result)