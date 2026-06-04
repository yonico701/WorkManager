import mysql.connector
from repositories.db_connection import get_db_connection
from models.Job import Job


def row_to_job(row):
    if row is None:
        return None



    return Job(
        job_id=row[0],
        customer_id=row[1],
        provider_id=row[2],
        job_type=row[3],
        description=row[4],
        address=row[5],
        price=float(row[6]),
        created_at=row[7],
        schedule_date=row[8],
        status=row[9]
    )

def create_job(job: Job):
    db_connection = None
    cursor = None
    try:
        db_connection = get_db_connection()
        if db_connection and db_connection.is_connected():
            cursor = db_connection.cursor()
            cursor.execute(
                "INSERT INTO `job` (job_id,customer_id,job_type,job_description,address,price,created_at,schedule_date ,provider_id ,job_status ) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                (job.job_id,
                 job.customer_id,
                 job.job_type,
                 job.description,
                 job.address,
                 job.price,
                 job.created_at,
                 job.schedule_date,
                 job.provider_id,
                 job.status)
            )
            db_connection.commit()
            return True
        return False
    except mysql.connector.Error as error:
        print("Failed to create job: {}".format(error))
        if db_connection and db_connection.is_connected():
            db_connection.rollback()
        return False

    finally:
        if cursor:
            cursor.close()
        if db_connection and db_connection.is_connected():
            db_connection.close()




def get_job_by_id(job_id):
    db_connection = None
    cursor = None

    try:

        db_connection = get_db_connection()
        if db_connection and db_connection.is_connected():
            cursor = db_connection.cursor()
            cursor.execute(
                "SELECT * FROM `job` WHERE  job_id=%s",
                (job_id,)
            )
            row = cursor.fetchone()

            if row is None:
                return None

            return row_to_job(row)

        return None


    except mysql.connector.Error as error:
        print("Failed to get job", error)
        return None

    finally:
        if cursor:
            cursor.close()
        if db_connection and db_connection.is_connected():
            db_connection.close()






def get_all_jobs():
    db_connection = None
    cursor = None

    try:

        db_connection = get_db_connection()
        if db_connection and db_connection.is_connected():
            cursor = db_connection.cursor()
            cursor.execute(
                "SELECT * FROM `job`")

            rows = cursor.fetchall()
            jobs = []

            for row in rows:
                jobs.append(row_to_job(row))

            return jobs

        return []


    except mysql.connector.Error as error:
        print("Failed to get all jobs", error)
        return []

    finally:
        if cursor:
            cursor.close()
        if db_connection and db_connection.is_connected():
            db_connection.close()






def get_jobs_by_status(job_status):
    db_connection = None
    cursor = None

    try:

        db_connection = get_db_connection()
        if db_connection and db_connection.is_connected():
            cursor = db_connection.cursor()
            cursor.execute(
                "SELECT * FROM `job` WHERE  job_status=%s",
                (job_status,)
            )
            rows = cursor.fetchall()
            jobs = []

            for row in rows:
                jobs.append(row_to_job(row))

            return jobs

        return []


    except mysql.connector.Error as error:
        print("Failed to get jobs by status", error)
        return []

    finally:
        if cursor:
            cursor.close()
        if db_connection and db_connection.is_connected():
            db_connection.close()




def get_jobs_by_customer(customer_id):
    db_connection = None
    cursor = None

    try:

        db_connection = get_db_connection()
        if db_connection and db_connection.is_connected():
            cursor = db_connection.cursor()
            cursor.execute(
                "SELECT * FROM `job` WHERE  customer_id=%s",
                (customer_id,)
            )
            rows = cursor.fetchall()
            jobs = []

            for row in rows:
                jobs.append(row_to_job(row))

            return jobs

        return []


    except mysql.connector.Error as error:
        print("Failed to get jobs by customer_id", error)
        return []

    finally:
        if cursor:
            cursor.close()
        if db_connection and db_connection.is_connected():
            db_connection.close()





def get_jobs_by_provider(provider_id):
    db_connection = None
    cursor = None

    try:

        db_connection = get_db_connection()
        if db_connection and db_connection.is_connected():
            cursor = db_connection.cursor()
            cursor.execute(
                "SELECT * FROM `job` WHERE  provider_id=%s",
                (provider_id,)
            )
            rows = cursor.fetchall()
            jobs = []

            for row in rows:
                jobs.append(row_to_job(row))

            return jobs

        return []


    except mysql.connector.Error as error:
        print("Failed to get jobs by provider_id", error)
        return []

    finally:
        if cursor:
            cursor.close()
        if db_connection and db_connection.is_connected():
            db_connection.close()





def update_job_price(job_id,new_price):
    db_connection = None
    cursor = None
    try:

        db_connection = get_db_connection()
        if db_connection and db_connection.is_connected():
            cursor = db_connection.cursor()
            cursor.execute(
                "UPDATE `job` SET `price` = %s WHERE `job_id` = %s",
                (new_price, job_id)

            )

            db_connection.commit()
            return True

        return False


    except mysql.connector.Error as error:
        print("Failed to update job price ", error)
        if db_connection and db_connection.is_connected():
            db_connection.rollback()
        return False


    finally:
        if cursor:
            cursor.close()
        if db_connection and db_connection.is_connected():
            db_connection.close()





def update_job_address(job_id,new_address):
    db_connection = None
    cursor = None
    try:

        db_connection = get_db_connection()
        if db_connection and db_connection.is_connected():
            cursor = db_connection.cursor()
            cursor.execute(
                "UPDATE `job` SET `address` = %s WHERE `job_id` = %s",
                (new_address, job_id)

            )

            db_connection.commit()
            return True

        return False


    except mysql.connector.Error as error:
        print("Failed to update job address ", error)
        if db_connection and db_connection.is_connected():
            db_connection.rollback()
        return False


    finally:
        if cursor:
            cursor.close()
        if db_connection and db_connection.is_connected():
            db_connection.close()





def update_job_description(job_id,description):
    db_connection = None
    cursor = None
    try:

        db_connection = get_db_connection()
        if db_connection and db_connection.is_connected():
            cursor = db_connection.cursor()
            cursor.execute(
                "UPDATE `job` SET `job_description` = %s WHERE `job_id` = %s",
                (description, job_id)

            )

            db_connection.commit()
            return True

        return False


    except mysql.connector.Error as error:
        print("Failed to update job description ", error)
        if db_connection and db_connection.is_connected():
            db_connection.rollback()
        return False


    finally:
        if cursor:
            cursor.close()
        if db_connection and db_connection.is_connected():
            db_connection.close()





def update_schedule_job(job_id,schedule_date):
    db_connection = None
    cursor = None
    try:

        db_connection = get_db_connection()
        if db_connection and db_connection.is_connected():
            cursor = db_connection.cursor()
            cursor.execute(
                "UPDATE `job` SET `schedule_date` = %s WHERE `job_id` = %s",
                (schedule_date, job_id)

            )

            db_connection.commit()
            return True

        return False


    except mysql.connector.Error as error:
        print("Failed to update job schedule_date ", error)
        if db_connection and db_connection.is_connected():
            db_connection.rollback()
        return False


    finally:
        if cursor:
            cursor.close()
        if db_connection and db_connection.is_connected():
            db_connection.close()





def assign_provider_to_job(job_id,provider_id):
    db_connection = None
    cursor = None
    try:

        db_connection = get_db_connection()
        if db_connection and db_connection.is_connected():
            cursor = db_connection.cursor()
            cursor.execute(
                "UPDATE `job` SET provider_id = %s, `job_status` = %s WHERE `job_id` = %s",
                (provider_id, "assigned", job_id)

            )

            db_connection.commit()
            return True

        return False


    except mysql.connector.Error as error:
        print("Failed to update job provider_id ", error)
        if db_connection and db_connection.is_connected():
            db_connection.rollback()
        return False


    finally:
        if cursor:
            cursor.close()
        if db_connection and db_connection.is_connected():
            db_connection.close()





def start_job(job_id):
    db_connection = None
    cursor = None
    try:

        db_connection = get_db_connection()
        if db_connection and db_connection.is_connected():
            cursor = db_connection.cursor()
            cursor.execute(
                "UPDATE `job` SET  `job_status` = %s WHERE `job_id` = %s",
                ("in_progress", job_id)

            )

            db_connection.commit()
            return True

        return False


    except mysql.connector.Error as error:
        print("Failed to update job_status to in progress ", error)
        if db_connection and db_connection.is_connected():
            db_connection.rollback()
        return False


    finally:
        if cursor:
            cursor.close()
        if db_connection and db_connection.is_connected():
            db_connection.close()




def cancel_job(job_id):
    db_connection = None
    cursor = None
    try:

        db_connection = get_db_connection()
        if db_connection and db_connection.is_connected():
            cursor = db_connection.cursor()
            cursor.execute(
                "UPDATE `job` SET  `job_status` = %s WHERE `job_id` = %s",
                ("cancelled", job_id)

            )

            db_connection.commit()
            return True

        return False


    except mysql.connector.Error as error:
        print("Failed to update job_status to cancelled ", error)
        if db_connection and db_connection.is_connected():
            db_connection.rollback()
        return False


    finally:
        if cursor:
            cursor.close()
        if db_connection and db_connection.is_connected():
            db_connection.close()






def complete_job(job_id):
    db_connection = None
    cursor = None
    try:

        db_connection = get_db_connection()
        if db_connection and db_connection.is_connected():
            cursor = db_connection.cursor()
            cursor.execute(
                "UPDATE `job` SET  `job_status` = %s WHERE `job_id` = %s",
                ("completed", job_id)

            )

            db_connection.commit()
            return True

        return False


    except mysql.connector.Error as error:
        print("Failed to update job_status to completed ", error)
        if db_connection and db_connection.is_connected():
            db_connection.rollback()
        return False


    finally:
        if cursor:
            cursor.close()
        if db_connection and db_connection.is_connected():
            db_connection.close()
