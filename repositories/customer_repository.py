import mysql.connector
from repositories.db_connection import get_db_connection
from models.Customer import Customer

def row_to_customer(row):
    if row is None:
        return None

    return Customer(user_id=row[0],
                    full_name=row[1],
                    phone_number=row[2],
                    email=row[3],
                    city=row[4],
                    is_active= bool(row[5]),
                    address=row[6],
                    notes=row[7])




def create_customer(customer:Customer):
    db_connection = None
    cursor = None
    try:

        db_connection = get_db_connection()
        if db_connection and db_connection.is_connected():
            cursor = db_connection.cursor()
            cursor.execute("INSERT INTO `user` (user_id,full_name,phone_number,email,city,is_active)  VALUES (%s,%s,%s,%s,%s,%s)",
                           (customer.user_id,
                            customer.full_name,
                            customer.phone_number,
                            customer.email,
                            customer.city,
                            customer.is_active)
                           )

            cursor.execute("INSERT INTO customer (user_id,address,notes) VALUES (%s,%s,%s)",
                           (customer.user_id,
                            customer.address,
                            customer.notes)
                           )
            db_connection.commit()
            return True

        return False


    except mysql.connector.Error as error:
        print("Failed to create customer", error)
        if db_connection and db_connection.is_connected():
            db_connection.rollback()
        return False


    finally:
        if cursor:
            cursor.close()
        if db_connection and db_connection.is_connected():
            db_connection.close()




def get_customer_by_id(user_id):
    db_connection = None
    cursor = None

    try:

        db_connection = get_db_connection()
        if db_connection and db_connection.is_connected():
            cursor = db_connection.cursor()
            cursor.execute(
                "SELECT user.user_id, "
                "user.full_name, "
                "user.phone_number, "
                "user.email, "
                "user.city, "
                "user.is_active, "
                "customer.address, "
                "customer.notes "
                "FROM user "
                "INNER JOIN customer ON user.user_id = customer.user_id "
                "WHERE user.user_id = %s",
                (user_id,)
            )
            row = cursor.fetchone()
            return row_to_customer(row)

        return None


    except mysql.connector.Error as error:
        print("Failed to get customer", error)
        return None

    finally:
        if cursor:
            cursor.close()
        if db_connection and db_connection.is_connected():
            db_connection.close()


def get_all_customers():
    db_connection = None
    cursor = None

    try:

        db_connection = get_db_connection()
        if db_connection and db_connection.is_connected():
            cursor = db_connection.cursor()
            cursor.execute(
                "SELECT user.user_id, "
                "user.full_name, "
                "user.phone_number, "
                "user.email, "
                "user.city, "
                "user.is_active, "
                "customer.address, "
                "customer.notes "
                "FROM user "
                "INNER JOIN customer ON user.user_id = customer.user_id "

            )
            rows = cursor.fetchall()
            customers=[]
            for row in rows:
                customers.append(row_to_customer(row))
            return customers

        return []


    except mysql.connector.Error as error:
        print("Failed to get all  customers", error)
        return []

    finally:
        if cursor:
            cursor.close()
        if db_connection and db_connection.is_connected():
            db_connection.close()





def update_customer_address(customer_id, address):
    db_connection = None
    cursor = None
    try:

        db_connection = get_db_connection()
        if db_connection and db_connection.is_connected():
            cursor = db_connection.cursor()
            cursor.execute(
                "UPDATE customer SET `address` = %s WHERE `user_id` = %s",(address,customer_id)

                )

            db_connection.commit()
            return True

        return False


    except mysql.connector.Error as error:
        print("Failed to update customer address", error)
        if db_connection and db_connection.is_connected():
            db_connection.rollback()
        return False


    finally:
        if cursor:
            cursor.close()
        if db_connection and db_connection.is_connected():
            db_connection.close()




def add_customer_notes(customer_id, notes):
    db_connection = None
    cursor = None
    try:

        db_connection = get_db_connection()
        if db_connection and db_connection.is_connected():
            cursor = db_connection.cursor()
            cursor.execute(
                "UPDATE customer SET `notes` = %s WHERE `user_id` = %s", (notes, customer_id)

            )

            db_connection.commit()
            return True

        return False


    except mysql.connector.Error as error:
        print("Failed to update customer notes", error)
        if db_connection and db_connection.is_connected():
            db_connection.rollback()
        return False


    finally:
        if cursor:
            cursor.close()
        if db_connection and db_connection.is_connected():
            db_connection.close()





def remove_customer_notes(customer_id):
    db_connection = None
    cursor = None
    try:

        db_connection = get_db_connection()
        if db_connection and db_connection.is_connected():
            cursor = db_connection.cursor()
            cursor.execute(
                "UPDATE customer SET `notes` = '' WHERE `user_id` = %s", (customer_id,)

            )

            db_connection.commit()
            return True

        return False


    except mysql.connector.Error as error:
        print("Failed to delete customer notes", error)
        if db_connection and db_connection.is_connected():
            db_connection.rollback()
        return False


    finally:
        if cursor:
            cursor.close()
        if db_connection and db_connection.is_connected():
            db_connection.close()


def activate_customer(customer_id):
    db_connection = None
    cursor = None
    try:

        db_connection = get_db_connection()
        if db_connection and db_connection.is_connected():
            cursor = db_connection.cursor()
            cursor.execute(
                "UPDATE `user` SET `is_active` = 1 WHERE `user_id` = %s", (customer_id,)

            )

            db_connection.commit()
            return True

        return False


    except mysql.connector.Error as error:
        print("activate customer failure", error)
        if db_connection and db_connection.is_connected():
            db_connection.rollback()
        return False


    finally:
        if cursor:
            cursor.close()
        if db_connection and db_connection.is_connected():
            db_connection.close()


def deactivate_customer(customer_id):
    db_connection = None
    cursor = None
    try:

        db_connection = get_db_connection()
        if db_connection and db_connection.is_connected():
            cursor = db_connection.cursor()
            cursor.execute(
                "UPDATE `user` SET `is_active` = 0 WHERE `user_id` = %s", (customer_id,)

            )

            db_connection.commit()
            return True

        return False


    except mysql.connector.Error as error:
        print("deactivate customer failure", error)
        if db_connection and db_connection.is_connected():
            db_connection.rollback()
        return False


    finally:
        if cursor:
            cursor.close()
        if db_connection and db_connection.is_connected():
            db_connection.close()




