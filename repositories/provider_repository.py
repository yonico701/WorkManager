import mysql.connector
from repositories.db_connection import get_db_connection
from models.ServiceProvider import ServiceProvider


def row_to_provider(row, professions):
    if row is None:
        return None

    profession_list = []

    for profession in professions:
        profession_list.append(profession[0])

    return ServiceProvider(
        user_id=row[0],
        full_name=row[1],
        phone_number=row[2],
        email=row[3],
        city=row[4],
        profession=profession_list,
        experience_years=row[7],
        base_price=float(row[8]),
        availability=bool(row[9]),
        is_active=bool(row[5])
    )


def create_provider(provider: ServiceProvider):
    db_connection = None
    cursor = None
    try:

        db_connection = get_db_connection()
        if db_connection and db_connection.is_connected():
            cursor = db_connection.cursor()
            cursor.execute(
                "INSERT INTO `user` (user_id,full_name,phone_number,email,city,is_active)  VALUES (%s,%s,%s,%s,%s,%s)",
                (provider.user_id,
                 provider.full_name,
                 provider.phone_number,
                 provider.email,
                 provider.city,
                 provider.is_active)
                )

            cursor.execute("INSERT INTO `provider` (user_id,experience_years,base_price,availability) VALUES (%s,%s,%s,%s)",
                           (provider.user_id,
                            provider.experience_years,
                            provider.base_price,
                            provider.availability)
                           )

            for profession in provider.profession:
                cursor.execute("INSERT INTO `provider_profession` (provider_id,profession) VALUES (%s,%s)",
                               (provider.user_id,
                               profession)
                               )
            db_connection.commit()
            return True

        return False






    except mysql.connector.Error as error:
        print("Failed to create provider", error)
        if db_connection and db_connection.is_connected():
            db_connection.rollback()
        return False


    finally:
        if cursor:
            cursor.close()
        if db_connection and db_connection.is_connected():
            db_connection.close()






def get_provider_by_id(user_id):
    db_connection = None
    cursor = None

    try:

        db_connection = get_db_connection()
        if db_connection and db_connection.is_connected():
            cursor = db_connection.cursor()
            cursor.execute(
                "SELECT * FROM `user` INNER JOIN provider ON `user`.user_id = provider.user_id WHERE  `user`.user_id=%s",
                (user_id,)
            )
            row = cursor.fetchone()

            if row is None:
                return None

            professions = get_provider_professions(user_id)

            return row_to_provider(row, professions)

        return None


    except mysql.connector.Error as error:
        print("Failed to get provider", error)
        return None

    finally:
        if cursor:
            cursor.close()
        if db_connection and db_connection.is_connected():
            db_connection.close()



def get_provider_professions(user_id):
    db_connection = None
    cursor = None

    try:

        db_connection = get_db_connection()
        if db_connection and db_connection.is_connected():
            cursor = db_connection.cursor()
            cursor.execute(
                "SELECT profession FROM `provider_profession` WHERE `provider_profession`.provider_id=%s",
                (user_id,)
            )
            provider = cursor.fetchall()
            return provider

        return None


    except mysql.connector.Error as error:
        print("Failed to get provider_profession", error)
        return None

    finally:
        if cursor:
            cursor.close()
        if db_connection and db_connection.is_connected():
            db_connection.close()





def get_all_providers():
    db_connection = None
    cursor = None

    try:

        db_connection = get_db_connection()
        if db_connection and db_connection.is_connected():
            cursor = db_connection.cursor()
            cursor.execute(
                "SELECT * FROM `user` INNER JOIN provider ON `user`.user_id = provider.user_id")

            rows = cursor.fetchall()
            providers = []

            for row in rows:
                professions = get_provider_professions(row[0])
                providers.append(row_to_provider(row, professions))

            return providers
        return []


    except mysql.connector.Error as error:
        print("Failed to get all provider", error)
        return []

    finally:
        if cursor:
            cursor.close()
        if db_connection and db_connection.is_connected():
            db_connection.close()



def update_provider_base_price(provider_id,base_price):
    db_connection = None
    cursor = None
    try:

        db_connection = get_db_connection()
        if db_connection and db_connection.is_connected():
            cursor = db_connection.cursor()
            cursor.execute(
                "UPDATE provider SET `base_price` = %s WHERE `user_id` = %s",
                (base_price, provider_id)

            )

            db_connection.commit()
            return True

        return False


    except mysql.connector.Error as error:
        print("Failed to update provider base_price ", error)
        if db_connection and db_connection.is_connected():
            db_connection.rollback()
        return False


    finally:
        if cursor:
            cursor.close()
        if db_connection and db_connection.is_connected():
            db_connection.close()



def add_provider_profession(provider_id,profession):
    db_connection = None
    cursor = None
    try:

        db_connection = get_db_connection()
        if db_connection and db_connection.is_connected():
            cursor = db_connection.cursor()
            cursor.execute(
                "INSERT INTO `provider_profession` (provider_id, profession) VALUES (%s, %s)",
                (provider_id, profession)
            )

            db_connection.commit()
            return True

        return False


    except mysql.connector.Error as error:
        print("Failed to add profession ", error)
        if db_connection and db_connection.is_connected():
            db_connection.rollback()
        return False


    finally:
        if cursor:
            cursor.close()
        if db_connection and db_connection.is_connected():
            db_connection.close()



def mark_provider_availability(provider_id):
    db_connection = None
    cursor = None
    try:

        db_connection = get_db_connection()
        if db_connection and db_connection.is_connected():
            cursor = db_connection.cursor()
            cursor.execute(
                "UPDATE `provider` SET `availability` = 1 WHERE `user_id` = %s", (provider_id,)

            )

            db_connection.commit()
            return True

        return False


    except mysql.connector.Error as error:
        print("availability provider failure", error)
        if db_connection and db_connection.is_connected():
            db_connection.rollback()
        return False


    finally:
        if cursor:
            cursor.close()
        if db_connection and db_connection.is_connected():
            db_connection.close()




def mark_provider_unavailability(provider_id):
    db_connection = None
    cursor = None
    try:

        db_connection = get_db_connection()
        if db_connection and db_connection.is_connected():
            cursor = db_connection.cursor()
            cursor.execute(
                "UPDATE `provider` SET `availability` = 0 WHERE `user_id` = %s", (provider_id,)

            )

            db_connection.commit()
            return True

        return False


    except mysql.connector.Error as error:
        print("unavailability provider failure", error)
        if db_connection and db_connection.is_connected():
            db_connection.rollback()
        return False


    finally:
        if cursor:
            cursor.close()
        if db_connection and db_connection.is_connected():
            db_connection.close()




def activate_provider(provider_id):
    db_connection = None
    cursor = None
    try:

        db_connection = get_db_connection()
        if db_connection and db_connection.is_connected():
            cursor = db_connection.cursor()
            cursor.execute(
                "UPDATE `user` SET `is_active` = 1 WHERE `user_id` = %s", (provider_id,)

            )

            db_connection.commit()
            return True

        return False


    except mysql.connector.Error as error:
        print("activate provider failure", error)
        if db_connection and db_connection.is_connected():
            db_connection.rollback()
        return False


    finally:
        if cursor:
            cursor.close()
        if db_connection and db_connection.is_connected():
            db_connection.close()


def deactivate_provider(provider_id):
    db_connection = None
    cursor = None
    try:

        db_connection = get_db_connection()
        if db_connection and db_connection.is_connected():
            cursor = db_connection.cursor()
            cursor.execute(
                "UPDATE `user` SET `is_active` = 0 WHERE `user_id` = %s", (provider_id,)

            )

            db_connection.commit()
            return True

        return False


    except mysql.connector.Error as error:
        print("deactivate provider failure", error)
        if db_connection and db_connection.is_connected():
            db_connection.rollback()
        return False


    finally:
        if cursor:
            cursor.close()
        if db_connection and db_connection.is_connected():
            db_connection.close()

