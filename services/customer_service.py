import repositories.customer_repository as customer_repo
from models.Customer import Customer
import repositories.job_repository as job_repo



def get_all_customers():
    customers = customer_repo.get_all_customers()

    if customers is None:
        raise ValueError("failed to get customers")

    return customers





def create_customer(data):
    customer = Customer(**data)

    existing_customer = customer_repo.get_customer_by_id(customer.user_id)

    if existing_customer is not None:
        raise ValueError("customer already exists")

    success = customer_repo.create_customer(customer)

    if not success:
        raise ValueError("customer creation failed")

    return customer




def validate_customer_id(customer_id):

    if not isinstance(customer_id, str):
        raise TypeError("customer_id must be a string")

    customer_id = customer_id.strip()

    if customer_id == "":
        raise ValueError("customer_id cannot be empty")

    return customer_id


def get_customer_by_id(customer_id):

    customer_id = validate_customer_id(customer_id)

    customer = customer_repo.get_customer_by_id(customer_id)

    if customer is None:
        return None

    return customer





def get_jobs_by_customer(customer_id):
    customer = get_customer_by_id(customer_id)

    if customer is None:
        raise ValueError("customer not found")

    jobs = job_repo.get_jobs_by_customer(customer_id)

    if jobs is None:
        raise ValueError("failed to get customer jobs")

    return jobs




def update_customer_address(customer_id, new_address):

    customer = get_customer_by_id(customer_id)

    if customer is None:
        raise ValueError("customer not found")

    customer.update_address(new_address)

    success = customer_repo.update_customer_address(
        customer_id,
        customer.address
    )

    if not success:
        raise ValueError("customer address update failed")

    return customer





def update_customer_notes(customer_id, new_notes):

    customer = get_customer_by_id(customer_id)

    if customer is None:
        raise ValueError("customer not found")

    customer.add_notes(new_notes)

    success = customer_repo.add_customer_notes(
        customer_id,
        customer.notes
    )

    if not success:
        raise ValueError("customer notes update failed")

    return customer







def delete_customer_notes(customer_id):
    customer = get_customer_by_id(customer_id)

    if customer is None:
        raise ValueError("customer not found")

    customer.remove_notes()

    success = customer_repo.remove_customer_notes(customer_id)

    if not success:
        raise ValueError("customer notes delete failed")

    return customer




def activate_customer(customer_id):

    customer = get_customer_by_id(customer_id)

    if customer is None:
        raise ValueError("customer not found")

    customer.active()

    success = customer_repo.activate_customer(customer_id)

    if not success:
        raise ValueError("customer activation failed")

    return customer





def deactivate_customer(customer_id):

    customer = get_customer_by_id(customer_id)

    if customer is None:
        raise ValueError("customer not found")

    customer.inactive()

    success = customer_repo.deactivate_customer(customer_id)

    if not success:
        raise ValueError("customer deactivation failed")

    return customer