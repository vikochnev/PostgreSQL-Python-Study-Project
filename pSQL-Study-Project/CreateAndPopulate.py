import psycopg2
from psycopg2 import Error
import create_and_pop_queries as dt
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


connection = create_db_connection(user_name="postgres",
                                  user_password=password.user_password,
                                  host_address="127.0.0.1",
                                  server_port="5432",
                                  db_name="school")


# creates tables
execute_query(connection, dt.create_teacher_table)
execute_query(connection, dt.create_client_table)
execute_query(connection, dt.create_participant_table)
execute_query(connection, dt.create_course_table)

# adds relations (via foreign keys) to tables
execute_query(connection, dt.alter_participant)
execute_query(connection, dt.alter_course)
execute_query(connection, dt.alter_course_again)
execute_query(connection, dt.create_takescourse_table)

# populates tables
execute_query(connection, dt.pop_teacher)
execute_query(connection, dt.pop_client)
execute_query(connection, dt.pop_participant)
execute_query(connection, dt.pop_course)
execute_query(connection, dt.pop_takescourse)