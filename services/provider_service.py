from models.ServiceProvider import ServiceProvider
import repositories.provider_repository as provider_repo
import repositories.job_repository as job_repo


def validate_provider_id(provider_id):

    if not isinstance(provider_id, str):
        raise TypeError("provider_id must be a string")

    provider_id = provider_id.strip()

    if provider_id == "":
        raise ValueError("provider_id cannot be empty")

    return provider_id


def get_all_providers():

    providers = provider_repo.get_all_providers()

    if providers is None:
        raise ValueError("failed to get providers")

    return providers


def get_provider_by_id(provider_id):

    provider_id = validate_provider_id(provider_id)

    provider = provider_repo.get_provider_by_id(provider_id)

    if provider is None:
        return None

    return provider


def get_jobs_by_provider(provider_id):

    provider = get_provider_by_id(provider_id)

    if provider is None:
        raise ValueError("provider not found")

    jobs = job_repo.get_jobs_by_provider(provider_id)

    if jobs is None:
        raise ValueError("failed to get provider jobs")

    return jobs


def create_provider(data):

    provider = ServiceProvider(**data)

    existing_provider = provider_repo.get_provider_by_id(provider.user_id)

    if existing_provider is not None:
        raise ValueError("provider already exists")

    success = provider_repo.create_provider(provider)

    if not success:
        raise ValueError("provider creation failed")

    return provider


def update_provider_base_price(provider_id, new_base_price):

    provider = get_provider_by_id(provider_id)

    if provider is None:
        raise ValueError("provider not found")

    provider.update_base_price(new_base_price)

    success = provider_repo.update_provider_base_price(
        provider_id,
        provider.base_price
    )

    if not success:
        raise ValueError("provider base price update failed")

    return provider


def add_provider_profession(provider_id, new_profession):

    provider = get_provider_by_id(provider_id)

    if provider is None:
        raise ValueError("provider not found")

    provider.add_profession(new_profession)

    success = provider_repo.add_provider_profession(
        provider_id,
        new_profession
    )

    if not success:
        raise ValueError("provider profession update failed")

    return provider


def mark_provider_availability(provider_id):

    provider = get_provider_by_id(provider_id)

    if provider is None:
        raise ValueError("provider not found")

    provider.mark_availability()

    success = provider_repo.mark_provider_availability(provider_id)

    if not success:
        raise ValueError("provider availability update failed")

    return provider


def mark_provider_unavailability(provider_id):

    provider = get_provider_by_id(provider_id)

    if provider is None:
        raise ValueError("provider not found")

    provider.mark_unavailability()

    success = provider_repo.mark_provider_unavailability(provider_id)

    if not success:
        raise ValueError("provider unavailability update failed")

    return provider


def activate_provider(provider_id):

    provider = get_provider_by_id(provider_id)

    if provider is None:
        raise ValueError("provider not found")

    provider.active()

    success = provider_repo.activate_provider(provider_id)

    if not success:
        raise ValueError("provider activation failed")

    return provider


def deactivate_provider(provider_id):

    provider = get_provider_by_id(provider_id)

    if provider is None:
        raise ValueError("provider not found")

    provider.inactive()

    success = provider_repo.deactivate_provider(provider_id)

    if not success:
        raise ValueError("provider deactivation failed")

    return provider

