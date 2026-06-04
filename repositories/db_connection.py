import mysql.connector

def get_db_connection():
    try:
        db_connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Yc20240212!@",
            database="workmanegment_db",

        )
        return db_connection

    except mysql.connector.Error as error:
        print("Failed to create database connection to MySQL database", error)






if __name__ == "__main__":
    connection = get_db_connection()

    if connection:
        print("Connected successfully to MySQL!")
        connection.close()




