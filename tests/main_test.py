from datetime import datetime, timedelta

from models.User import User
from models.Customer import Customer
from models.ServiceProvider import ServiceProvider
from models.Job import Job
from services.System import System
from storage.json_storage import save_to_json


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


def expected_fail(test_name, func):
    try:
        func()
        print(f"[FAIL] {test_name} -> expected error but no error was raised")
    except Exception as e:
        print(f"[PASS] {test_name} -> caught expected {type(e).__name__}: {e}")


def assert_equal(actual, expected):
    if actual != expected:
        raise AssertionError(f"Expected {expected}, got {actual}")


def assert_not_none(value):
    if value is None:
        raise AssertionError("Expected value but got None")


def assert_true(value):
    if value is not True:
        raise AssertionError("Expected True")


def assert_false(value):
    if value is not False:
        raise AssertionError("Expected False")


def print_list(items):
    if not items:
        print("Empty list")
    for item in items:
        print("-" * 30)
        print(item)


def main():
    print_section("START FULL PROFESSIONAL WORK MANAGER TEST")

    # ============================================================
    # 1. USER TESTS
    # ============================================================
    print_section("1. USER TESTS")

    pass_test(
        "Create valid User",
        lambda: User("u1", "Test User", "0521234567", "test@gmail.com", "Netanya")
    )

    expected_fail(
        "User id not string should fail",
        lambda: User(1, "Test User", "0521234567", "test@gmail.com", "Netanya")
    )

    expected_fail(
        "Empty full name should fail",
        lambda: User("u1", "   ", "0521234567", "test@gmail.com", "Netanya")
    )

    expected_fail(
        "Invalid phone should fail",
        lambda: User("u1", "Test User", "123", "test@gmail.com", "Netanya")
    )

    expected_fail(
        "Invalid email should fail",
        lambda: User("u1", "Test User", "0521234567", "bad_email", "Netanya")
    )

    expected_fail(
        "is_active not boolean should fail",
        lambda: User("u1", "Test User", "0521234567", "test@gmail.com", "Netanya", "yes")
    )

    user = User("u2", "Active Test", "0527654321", "active@gmail.com", "Haifa")

    pass_test("Deactivate user", lambda: user.inactive())
    pass_test("Check user inactive", lambda: assert_false(user.is_active))
    pass_test("Activate user", lambda: user.active())
    pass_test("Check user active", lambda: assert_true(user.is_active))

    # ============================================================
    # 2. CUSTOMER TESTS
    # ============================================================
    print_section("2. CUSTOMER TESTS")

    customer = Customer(
        "c1",
        "Yonatan Cohen",
        "0521234567",
        "yonatan@gmail.com",
        "Netanya",
        "Herzl 10"
    )

    pass_test("Create valid Customer", lambda: assert_equal(customer.address, "Herzl 10"))

    expected_fail(
        "Customer empty address should fail",
        lambda: Customer("c2", "Bad Customer", "0521111111", "bad@gmail.com", "Tel Aviv", "   ")
    )

    expected_fail(
        "Customer job_history not list should fail",
        lambda: Customer("c2", "Bad Customer", "0521111111", "bad@gmail.com", "Tel Aviv", "Street", "job_1")
    )

    expected_fail(
        "Customer notes not string should fail",
        lambda: Customer("c2", "Bad Customer", "0521111111", "bad@gmail.com", "Tel Aviv", "Street", None, 123)
    )

    pass_test("Customer add job history", lambda: customer.add_job_history("job_100"))
    pass_test("Check customer job history", lambda: assert_equal(customer.job_history, ["job_100"]))

    expected_fail(
        "Customer add empty job history should fail",
        lambda: customer.add_job_history("   ")
    )

    pass_test("Customer add notes", lambda: customer.add_notes("Important customer"))
    pass_test("Check customer notes contains text", lambda: assert_equal(customer.notes.strip(), "Important customer"))

    expected_fail(
        "Customer add empty notes should fail",
        lambda: customer.add_notes("   ")
    )

    pass_test("Customer remove notes", lambda: customer.remove_notes())
    pass_test("Check customer notes removed", lambda: assert_equal(customer.notes, ""))

    pass_test("Customer update address", lambda: customer.update_address("New Address 20"))
    pass_test("Check customer new address", lambda: assert_equal(customer.address, "New Address 20"))

    expected_fail(
        "Customer update empty address should fail",
        lambda: customer.update_address("   ")
    )

    # ============================================================
    # 3. SERVICE PROVIDER TESTS
    # ============================================================
    print_section("3. SERVICE PROVIDER TESTS")

    provider = ServiceProvider(
        "p1",
        "Moshe Plumbing",
        "0501111111",
        "moshe@gmail.com",
        "Netanya",
        ["plumbing"],
        10,
        250
    )

    pass_test("Create valid ServiceProvider", lambda: assert_equal(provider.profession, ["plumbing"]))

    expected_fail(
        "Provider profession not list should fail",
        lambda: ServiceProvider("p2", "Bad Provider", "0502222222", "bad@gmail.com", "Haifa", "plumbing", 5, 200)
    )

    expected_fail(
        "Provider empty profession list should fail",
        lambda: ServiceProvider("p2", "Bad Provider", "0502222222", "bad@gmail.com", "Haifa", [], 5, 200)
    )

    expected_fail(
        "Provider invalid profession should fail",
        lambda: ServiceProvider("p2", "Bad Provider", "0502222222", "bad@gmail.com", "Haifa", ["gardening"], 5, 200)
    )

    expected_fail(
        "Provider negative experience should fail",
        lambda: ServiceProvider("p2", "Bad Provider", "0502222222", "bad@gmail.com", "Haifa", ["plumbing"], -1, 200)
    )

    expected_fail(
        "Provider negative base price should fail",
        lambda: ServiceProvider("p2", "Bad Provider", "0502222222", "bad@gmail.com", "Haifa", ["plumbing"], 5, -10)
    )

    expected_fail(
        "Provider availability not boolean should fail",
        lambda: ServiceProvider("p2", "Bad Provider", "0502222222", "bad@gmail.com", "Haifa", ["plumbing"], 5, 200, None, "yes")
    )

    pass_test("Provider add profession", lambda: provider.add_profession("electricity"))
    pass_test("Check provider profession added", lambda: assert_equal(provider.profession, ["plumbing", "electricity"]))

    expected_fail(
        "Provider duplicate profession should fail",
        lambda: provider.add_profession("plumbing")
    )

    expected_fail(
        "Provider invalid added profession should fail",
        lambda: provider.add_profession("gardening")
    )

    pass_test("Provider update base price", lambda: provider.update_base_price(300))
    pass_test("Check provider new base price", lambda: assert_equal(provider.base_price, 300))

    expected_fail(
        "Provider update negative base price should fail",
        lambda: provider.update_base_price(-20)
    )

    pass_test("Provider add completed job", lambda: provider.add_completing_job("job_200"))
    pass_test("Check provider completed jobs", lambda: assert_equal(provider.completing_jobs, ["job_200"]))

    expected_fail(
        "Provider add empty completed job should fail",
        lambda: provider.add_completing_job("   ")
    )

    pass_test("Provider mark unavailable", lambda: provider.mark_unavailability())
    pass_test("Check provider unavailable", lambda: assert_false(provider.availability))

    pass_test("Provider mark available", lambda: provider.mark_availability())
    pass_test("Check provider available", lambda: assert_true(provider.availability))

    # ============================================================
    # 4. DIRECT JOB TESTS
    # ============================================================
    print_section("4. DIRECT JOB TESTS")

    job = Job(
        "j1",
        "c1",
        "plumbing",
        "Fix sink",
        "Herzl 10",
        400,
        datetime.now()
    )

    pass_test("Create valid Job", lambda: assert_equal(job.status, "open"))

    expected_fail(
        "Job empty id should fail",
        lambda: Job("   ", "c1", "plumbing", "Fix sink", "Herzl 10", 400, datetime.now())
    )

    expected_fail(
        "Job invalid type should fail",
        lambda: Job("j2", "c1", "gaming", "Fix sink", "Herzl 10", 400, datetime.now())
    )

    expected_fail(
        "Job empty description should fail",
        lambda: Job("j2", "c1", "plumbing", "   ", "Herzl 10", 400, datetime.now())
    )

    expected_fail(
        "Job negative price should fail",
        lambda: Job("j2", "c1", "plumbing", "Fix sink", "Herzl 10", -1, datetime.now())
    )

    expected_fail(
        "Job created_at not datetime should fail",
        lambda: Job("j2", "c1", "plumbing", "Fix sink", "Herzl 10", 400, "today")
    )

    expected_fail(
        "Job assigned without provider should fail",
        lambda: Job("j2", "c1", "plumbing", "Fix sink", "Herzl 10", 400, datetime.now(), None, None, "assigned")
    )

    pass_test("Job assign provider", lambda: job.assign_provider("p1"))
    pass_test("Check job assigned status", lambda: assert_equal(job.status, "assigned"))
    pass_test("Job start", lambda: job.start_job())
    pass_test("Check job in progress", lambda: assert_equal(job.status, "in_progress"))
    pass_test("Job complete", lambda: job.complete_job())
    pass_test("Check job completed", lambda: assert_equal(job.status, "completed"))

    expected_fail(
        "Completed job cannot be cancelled",
        lambda: job.cancel_job()
    )

    job_for_update = Job(
        "j_update",
        "c1",
        "cleaning",
        "Clean house",
        "Old Address",
        200,
        datetime.now()
    )

    pass_test("Job schedule future date", lambda: job_for_update.schedule_job(datetime.now() + timedelta(days=2)))
    expected_fail("Job schedule past date should fail", lambda: job_for_update.schedule_job(datetime.now() - timedelta(days=1)))

    pass_test("Job update price", lambda: job_for_update.update_price(500))
    pass_test("Check job updated price", lambda: assert_equal(job_for_update.price, 500))

    expected_fail("Job update zero price should fail", lambda: job_for_update.update_price(0))

    pass_test("Job update description", lambda: job_for_update.update_description("Deep cleaning"))
    pass_test("Check job updated description", lambda: assert_equal(job_for_update.description, "Deep cleaning"))

    expected_fail("Job update empty description should fail", lambda: job_for_update.update_description("   "))

    pass_test("Job update address", lambda: job_for_update.update_address("New Address 100"))
    pass_test("Check job updated address", lambda: assert_equal(job_for_update.address, "New Address 100"))

    expected_fail("Job update empty address should fail", lambda: job_for_update.update_address("   "))

    # ============================================================
    # 5. SYSTEM FULL FLOW TESTS
    # ============================================================
    print_section("5. SYSTEM FULL FLOW TESTS")

    system = System()

    customer1 = Customer(
        "c1",
        "Yonatan Cohen",
        "0521234567",
        "yonatan@gmail.com",
        "Netanya",
        "Herzl 10"
    )

    customer2 = Customer(
        "c2",
        "David Levi",
        "0537654321",
        "david@gmail.com",
        "Tel Aviv",
        "Dizengoff 50"
    )

    provider1 = ServiceProvider(
        "p1",
        "Moshe Plumbing",
        "0501111111",
        "moshe@gmail.com",
        "Netanya",
        ["plumbing"],
        10,
        250
    )

    provider2 = ServiceProvider(
        "p2",
        "Avi Electric",
        "0502222222",
        "avi@gmail.com",
        "Haifa",
        ["electricity", "cleaning"],
        6,
        180
    )

    provider3 = ServiceProvider(
        "p3",
        "Inactive Provider",
        "0503333333",
        "inactive@gmail.com",
        "Ashdod",
        ["painting"],
        3,
        150
    )

    provider4 = ServiceProvider(
        "p4",
        "Unavailable Provider",
        "0504444444",
        "unavailable@gmail.com",
        "Jerusalem",
        ["cleaning"],
        4,
        170
    )

    pass_test("System add customer1", lambda: system.add_customer(customer1))
    pass_test("System add customer2", lambda: system.add_customer(customer2))
    pass_test("System add provider1", lambda: system.add_provider(provider1))
    pass_test("System add provider2", lambda: system.add_provider(provider2))
    pass_test("System add provider3", lambda: system.add_provider(provider3))
    pass_test("System add provider4", lambda: system.add_provider(provider4))

    expected_fail("System duplicate customer should fail", lambda: system.add_customer(customer1))
    expected_fail("System duplicate provider should fail", lambda: system.add_provider(provider1))

    expected_fail(
        "System customer id already exists in providers should fail",
        lambda: system.add_customer(Customer("p1", "Same Id", "0529999999", "same@gmail.com", "Netanya", "Address"))
    )

    expected_fail(
        "System provider id already exists in customers should fail",
        lambda: system.add_provider(ServiceProvider("c1", "Same Id Provider", "0509999999", "samep@gmail.com", "Netanya", ["plumbing"], 1, 100))
    )

    pass_test("System find customer", lambda: assert_not_none(system.find_customer("c1")))
    pass_test("System find provider", lambda: assert_not_none(system.find_provider("p1")))

    expected_fail("System find customer empty id should fail", lambda: system.find_customer("   "))
    expected_fail("System find provider empty id should fail", lambda: system.find_provider("   "))

    job1 = system.create_job("c1", "plumbing", "Fix leaking sink", "Herzl 10", 400)
    job2 = system.create_job("c2", "electricity", "Fix power outlet", "Dizengoff 50", 350)
    job3 = system.create_job("c1", "cleaning", "Clean apartment", "Herzl 10", 200)
    job4 = system.create_job("c2", "painting", "Paint room", "Dizengoff 50", 500)

    pass_test("Check job counter created job_1", lambda: assert_equal(job1.job_id, "job_1"))
    pass_test("Check job counter created job_4", lambda: assert_equal(job4.job_id, "job_4"))

    pass_test("Customer1 job history updated", lambda: assert_equal(customer1.job_history, ["job_1", "job_3"]))
    pass_test("Customer2 job history updated", lambda: assert_equal(customer2.job_history, ["job_2", "job_4"]))

    expected_fail(
        "System create job for missing customer should fail",
        lambda: system.create_job("bad_customer", "plumbing", "Bad job", "Address", 100)
    )

    expected_fail(
        "System create job invalid type should fail",
        lambda: system.create_job("c1", "bad_type", "Bad job", "Address", 100)
    )

    pass_test("Assign provider1 to job1", lambda: system.assign_provider_to_job(job1.job_id, "p1"))
    pass_test("Assign provider2 to job2", lambda: system.assign_provider_to_job(job2.job_id, "p2"))

    expected_fail(
        "Assign wrong profession should fail",
        lambda: system.assign_provider_to_job(job4.job_id, "p1")
    )

    provider3.inactive()
    expected_fail(
        "Assign inactive provider should fail",
        lambda: system.assign_provider_to_job(job4.job_id, "p3")
    )

    provider3.active()
    pass_test("Provider3 active again", lambda: assert_true(provider3.is_active))

    provider4.mark_unavailability()
    expected_fail(
        "Assign unavailable provider should fail",
        lambda: system.assign_provider_to_job(job3.job_id, "p4")
    )

    provider4.mark_availability()
    pass_test("Provider4 available again", lambda: assert_true(provider4.availability))

    expected_fail(
        "Assign non-existing job should fail",
        lambda: system.assign_provider_to_job("bad_job", "p1")
    )

    expected_fail(
        "Assign non-existing provider should fail",
        lambda: system.assign_provider_to_job(job3.job_id, "bad_provider")
    )

    expected_fail(
        "Assign provider to already assigned job should fail",
        lambda: system.assign_provider_to_job(job1.job_id, "p1")
    )

    pass_test("Start job1", lambda: system.start_job(job1.job_id))
    pass_test("Check job1 in progress", lambda: assert_equal(job1.status, "in_progress"))

    expected_fail(
        "Start open job should fail",
        lambda: system.start_job(job3.job_id)
    )

    expected_fail(
        "Start non-existing job should fail",
        lambda: system.start_job("bad_job")
    )

    pass_test("Complete job1", lambda: system.complete_job(job1.job_id))
    pass_test("Check job1 completed", lambda: assert_equal(job1.status, "completed"))
    pass_test("Check provider1 completed jobs updated", lambda: assert_equal(provider1.completing_jobs, ["job_1"]))

    expected_fail(
        "Complete assigned but not started job should fail",
        lambda: system.complete_job(job2.job_id)
    )

    expected_fail(
        "Complete non-existing job should fail",
        lambda: system.complete_job("bad_job")
    )

    expected_fail(
        "Cancel completed job should fail",
        lambda: system.cancel_job(job1.job_id)
    )

    pass_test("Cancel open job3", lambda: system.cancel_job(job3.job_id))
    pass_test("Check job3 cancelled", lambda: assert_equal(job3.status, "cancelled"))

    expected_fail(
        "Cancel cancelled job should fail",
        lambda: system.cancel_job(job3.job_id)
    )

    expected_fail(
        "Cancel non-existing job should fail",
        lambda: system.cancel_job("bad_job")
    )

    # ============================================================
    # 6. SYSTEM LIST AND REPORT TESTS
    # ============================================================
    print_section("6. SYSTEM LIST AND REPORT TESTS")

    pass_test("Show all customers", lambda: print_list(system.show_all_customers()))
    pass_test("Show all providers", lambda: print_list(system.show_all_providers()))
    pass_test("Show all jobs", lambda: print_list(system.show_all_jobs()))
    pass_test("Show open jobs", lambda: print_list(system.show_all_open_jobs()))
    pass_test("Show completed jobs", lambda: print_list(system.show_all_completed_jobs()))

    pass_test("Get jobs by customer c1", lambda: print_list(system.get_jobs_by_customer("c1")))
    pass_test("Get jobs by provider p1", lambda: print_list(system.get_jobs_by_provider("p1")))

    expected_fail(
        "Get jobs by missing customer should fail",
        lambda: system.get_jobs_by_customer("missing")
    )

    expected_fail(
        "Get jobs by missing provider should fail",
        lambda: system.get_jobs_by_provider("missing")
    )

    # ============================================================
    # 7. TO_DICT TESTS
    # ============================================================
    print_section("7. TO_DICT TESTS")

    pass_test("User to_dict", lambda: print(User("u_dict", "Dict User", "0525555555", "dict@gmail.com", "Netanya").to_dict()))
    pass_test("Customer to_dict", lambda: print(customer1.to_dict()))
    pass_test("Provider to_dict", lambda: print(provider1.to_dict()))
    pass_test("Job to_dict", lambda: print(job1.to_dict()))

    # ============================================================
    # 8. FINAL STATE
    # ============================================================
    print_section("8. FINAL STATE")

    print("Customers count:", len(system.customers))
    print("Providers count:", len(system.providers))
    print("Jobs count:", len(system.jobs))

    print("Customer c1 history:", customer1.job_history)
    print("Customer c2 history:", customer2.job_history)

    print("Provider p1 completed jobs:", provider1.completing_jobs)
    print("Provider p2 completed jobs:", provider2.completing_jobs)

    print("Job1 status:", job1.status)
    print("Job2 status:", job2.status)
    print("Job3 status:", job3.status)
    print("Job4 status:", job4.status)

    system.save_all_data()
    new_system = System()
    new_system.load_all_data()

    pass_test("Load customers from JSON", lambda: assert_equal(len(new_system.customers), len(system.customers)))
    pass_test("Load providers from JSON", lambda: assert_equal(len(new_system.providers), len(system.providers)))
    pass_test("Load jobs from JSON", lambda: assert_equal(len(new_system.jobs), len(system.jobs)))

    pass_test("Loaded customer c1 exists", lambda: assert_not_none(new_system.find_customer("c1")))
    pass_test("Loaded provider p1 exists", lambda: assert_not_none(new_system.find_provider("p1")))
    pass_test("Loaded job_1 exists", lambda: assert_not_none(new_system.find_job("job_1")))

    print_section("END FULL PROFESSIONAL WORK MANAGER TEST")


if __name__ == "__main__":
    main()