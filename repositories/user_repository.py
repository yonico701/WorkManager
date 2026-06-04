import mysql.connector
from repositories.db_connection import get_db_connection


def get_all_users():
    db_connection = None
    cursor = None

    try:


        db_connection = get_db_connection()
        if db_connection and db_connection.is_connected():
            cursor = db_connection.cursor()
            cursor.execute("SELECT * FROM `user`")
            users = cursor.fetchall()
            return users

        return []


    except mysql.connector.Error as error:
        print("Failed to get all users", error)
        return []

    finally:
        if cursor :
            cursor.close()
        if db_connection and db_connection.is_connected() :
            db_connection.close()



def get_user_by_id(user_id):
    db_connection = None
    cursor = None

    try:

        db_connection = get_db_connection()
        if db_connection and db_connection.is_connected():
            cursor = db_connection.cursor()
            cursor.execute(
                "SELECT * FROM `user` where `user_id`=%s",
                (user_id,)
            )
            user = cursor.fetchone()
            return user

        return None


    except mysql.connector.Error as error:
        print("Failed to get user", error)
        return None

    finally:
        if cursor:
            cursor.close()
        if db_connection and db_connection.is_connected():
            db_connection.close()


if __name__ == "__main__":
    print(get_all_users())
    print(get_user_by_id("c1",))