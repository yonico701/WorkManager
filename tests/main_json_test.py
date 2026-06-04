from datetime import datetime, timedelta
import os

from models.Customer import Customer
from models.ServiceProvider import ServiceProvider
from services.System import System
from storage.json_storage import save_to_json, load_from_json


TEST_FILE = "test_work_manager_data.json"


def print_section(title):
    print("\n" + "=" * 70)
    print(title)
    print("=" * 70)


def pass_test(test_name, func):
    try:
        func()
        print(f"[PASS] {test_name}")
    except Exception as e:
        print(f"[FAIL] {test_name} -> {type(e).__name__}: {e}")


def assert_equal(actual, expected):
    if actual != expected:
        raise AssertionError(f"Expected {expected}, got {actual}")


def assert_true(value):
    if value is not True:
        raise AssertionError("Expected True")


def assert_not_none(value):
    if value is None:
        raise AssertionError("Expected value but got None")


def delete_test_file():
    if os.path.exists(TEST_FILE):
        os.remove(TEST_FILE)


def build_test_system():
    system = System()

    customer1 = Customer(
        "c1", "Yonatan Cohen", "0521234567",
        "yonatan@gmail.com", "Netanya", "Herzl 10"
    )

    customer2 = Customer(
        "c2", "David Levi", "0537654321",
        "david@gmail.com", "Tel Aviv", "Dizengoff 50"
    )

    provider1 = ServiceProvider(
        "p1", "Moshe Plumbing", "0501111111",
        "moshe@gmail.com", "Netanya",
        ["plumbing"], 10, 250
    )

    provider2 = ServiceProvider(
        "p2", "Avi Electric", "0502222222",
        "avi@gmail.com", "Haifa",
        ["electricity", "cleaning"], 6, 180
    )

    system.add_customer(customer1)
    system.add_customer(customer2)
    system.add_provider(provider1)
    system.add_provider(provider2)

    job1 = system.create_job("c1", "plumbing", "Fix leaking sink", "Herzl 10", 400)
    job2 = system.create_job("c2", "electricity", "Fix power outlet", "Dizengoff 50", 350)
    job3 = system.create_job("c1", "cleaning", "Clean apartment", "Herzl 10", 200)

    system.assign_provider_to_job(job1.job_id, "p1")
    system.start_job(job1.job_id)
    system.complete_job(job1.job_id)

    system.assign_provider_to_job(job2.job_id, "p2")

    job3.schedule_job(datetime.now() + timedelta(days=1))

    return system


def system_to_json_data(system):
    return {
        "customers": [c.to_dict() for c in system.customers.values()],
        "providers": [p.to_dict() for p in system.providers.values()],
        "jobs": [j.to_dict() for j in system.jobs.values()]
    }


def validate_json_file_exists():
    data = load_from_json(TEST_FILE)
    assert_not_none(data)


def validate_json_structure():
    data = load_from_json(TEST_FILE)

    assert_true(isinstance(data, dict))
    assert_true("customers" in data)
    assert_true("providers" in data)
    assert_true("jobs" in data)

    assert_equal(len(data["customers"]), 2)
    assert_equal(len(data["providers"]), 2)
    assert_equal(len(data["jobs"]), 3)


def validate_loaded_json_data(data):
    customers = data["customers"]
    providers = data["providers"]
    jobs = data["jobs"]

    customer1 = customers[0]
    provider1 = providers[0]

    job1 = jobs[0]
    job2 = jobs[1]
    job3 = jobs[2]

    # Customer
    assert_equal(customer1["user_id"], "c1")
    assert_equal(customer1["full_name"], "Yonatan Cohen")
    assert_equal(customer1["job_history"], ["job_1", "job_3"])

    # Provider
    assert_equal(provider1["user_id"], "p1")
    assert_equal(provider1["full_name"], "Moshe Plumbing")
    assert_equal(provider1["completing_jobs"], ["job_1"])

    # Jobs
    assert_equal(job1["job_id"], "job_1")
    assert_equal(job1["status"], "completed")
    assert_equal(job1["provider_id"], "p1")

    assert_equal(job2["job_id"], "job_2")
    assert_equal(job2["status"], "assigned")
    assert_equal(job2["provider_id"], "p2")

    assert_equal(job3["job_id"], "job_3")
    assert_equal(job3["status"], "open")


def print_loaded_json_data(data):
    print("\nCustomers:")
    for c in data["customers"]:
        print(c)

    print("\nProviders:")
    for p in data["providers"]:
        print(p)

    print("\nJobs:")
    for j in data["jobs"]:
        print(j)


def main():
    print_section("START JSON STORAGE PROFESSIONAL TEST")

    delete_test_file()

    system = None
    loaded_data = None

    print_section("1. BUILD TEST SYSTEM")

    def create_system():
        nonlocal system
        system = build_test_system()

    pass_test("Create system", create_system)
    pass_test("Customers count", lambda: assert_equal(len(system.customers), 2))
    pass_test("Providers count", lambda: assert_equal(len(system.providers), 2))
    pass_test("Jobs count", lambda: assert_equal(len(system.jobs), 3))

    print_section("2. SAVE JSON")

    def save_test():
        data = system_to_json_data(system)
        save_to_json(TEST_FILE, data)

    pass_test("Save JSON", save_test)
    pass_test("JSON exists", validate_json_file_exists)
    pass_test("JSON structure", validate_json_structure)

    print_section("3. LOAD JSON")

    def load_test():
        nonlocal loaded_data
        loaded_data = load_from_json(TEST_FILE)

    pass_test("Load JSON", load_test)
    pass_test("Data exists", lambda: assert_not_none(loaded_data))
    pass_test("Validate JSON data", lambda: validate_loaded_json_data(loaded_data))

    print_section("4. PRINT DATA")
    pass_test("Print data", lambda: print_loaded_json_data(loaded_data))

    print_section("5. CLEANUP")
    pass_test("Delete file", delete_test_file)

    print_section("END TEST")


if __name__ == "__main__":
    main()