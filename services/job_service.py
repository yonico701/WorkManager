from datetime import datetime
from models.Job import Job, StatusList
import repositories.job_repository as job_repo
import repositories.customer_repository as customer_repo
import repositories.provider_repository as provider_repo


def validate_job_id(job_id):
    if not isinstance(job_id, str):
        raise TypeError("job_id must be a string")

    job_id = job_id.strip()

    if job_id == "":
        raise ValueError("job_id cannot be empty")

    return job_id


def get_job_by_id(job_id):
    job_id = validate_job_id(job_id)
    return job_repo.get_job_by_id(job_id)


def get_all_jobs(status=None):
    if status is not None:
        if not isinstance(status, str):
            raise TypeError("status must be a string")

        status = status.strip()

        if status == "":
            raise ValueError("status cannot be empty")

        if status not in StatusList:
            raise ValueError("status must be one of {}".format(StatusList))

        return job_repo.get_jobs_by_status(status)

    return job_repo.get_all_jobs()


def create_job(data):
    customer_id = data["customer_id"]

    customer = customer_repo.get_customer_by_id(customer_id)

    if customer is None:
        raise ValueError("customer not found")

    all_jobs = job_repo.get_all_jobs()
    job_id = "job_{}".format(len(all_jobs) + 1)

    created_at = datetime.now()

    new_job = Job(
        job_id=job_id,
        customer_id=customer_id,
        job_type=data["job_type"],
        description=data["description"],
        address=data["address"],
        price=data["price"],
        created_at=created_at
    )

    success = job_repo.create_job(new_job)

    if not success:
        raise ValueError("job creation failed")

    return new_job


def assign_provider_to_job(job_id, provider_id):
    job = get_job_by_id(job_id)

    if job is None:
        raise ValueError("job not found")

    provider = provider_repo.get_provider_by_id(provider_id)

    if provider is None:
        raise ValueError("provider not found")

    if job.status != "open":
        raise ValueError("job must be open")

    if not provider.is_active:
        raise ValueError("provider is not active")

    if not provider.availability:
        raise ValueError("provider is not available")

    if job.job_type not in provider.profession:
        raise ValueError("provider profession does not match job type")

    job.assign_provider(provider_id)

    success = job_repo.assign_provider_to_job(job.job_id, provider_id)

    if not success:
        raise ValueError("job assignment failed")

    return job


def start_job(job_id):
    job = get_job_by_id(job_id)

    if job is None:
        raise ValueError("job not found")

    job.start_job()

    success = job_repo.start_job(job.job_id)

    if not success:
        raise ValueError("job start failed")

    return job


def complete_job(job_id):
    job = get_job_by_id(job_id)

    if job is None:
        raise ValueError("job not found")

    job.complete_job()

    success = job_repo.complete_job(job.job_id)

    if not success:
        raise ValueError("job completion failed")

    return job


def cancel_job(job_id):
    job = get_job_by_id(job_id)

    if job is None:
        raise ValueError("job not found")

    job.cancel_job()

    success = job_repo.cancel_job(job.job_id)

    if not success:
        raise ValueError("job cancellation failed")

    return job


def update_job_price(job_id, new_price):
    job = get_job_by_id(job_id)

    if job is None:
        raise ValueError("job not found")

    job.update_price(new_price)

    success = job_repo.update_job_price(job.job_id, job.price)

    if not success:
        raise ValueError("job price update failed")

    return job


def update_job_address(job_id, new_address):
    job = get_job_by_id(job_id)

    if job is None:
        raise ValueError("job not found")

    job.update_address(new_address)

    success = job_repo.update_job_address(job.job_id, job.address)

    if not success:
        raise ValueError("job address update failed")

    return job


def update_job_description(job_id, new_description):
    job = get_job_by_id(job_id)

    if job is None:
        raise ValueError("job not found")

    job.update_description(new_description)

    success = job_repo.update_job_description(job.job_id, job.description)

    if not success:
        raise ValueError("job description update failed")

    return job


def update_job_schedule(job_id, schedule_date):
    job = get_job_by_id(job_id)

    if job is None:
        raise ValueError("job not found")

    if isinstance(schedule_date, str):
        schedule_date = datetime.fromisoformat(schedule_date)

    job.schedule_job(schedule_date)

    success = job_repo.update_schedule_job(job.job_id, job.schedule_date)

    if not success:
        raise ValueError("job schedule update failed")

    return job