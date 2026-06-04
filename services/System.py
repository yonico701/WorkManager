from models.Job import Job, StatusList
from models.ServiceProvider import ServiceProvider
from models.Customer import Customer
from datetime import datetime
from storage.json_storage import save_to_json , load_from_json





class System :
    def __init__(self):


        self.customers = {}
        self.providers = {}
        self.jobs = {}
        self.job_counter = 1


    ### customer ###

    def add_customer(self,customer):
        if not isinstance(customer,Customer):
            raise TypeError("Customer must be an instance of Customer")
        if customer.user_id in self.customers:
            raise ValueError("Customer already exists")
        if customer.user_id in self.providers:
            raise ValueError("Customer id already exists in providers")
        self.customers[customer.user_id] = customer

    def find_customer(self, user_id):
        if not isinstance(user_id, str):
            raise TypeError("User id must be an instance of str")
        user_id = user_id.strip()
        if user_id == "":
            raise ValueError("User id cannot be an empty string")
        if user_id not in self.customers:
            return None
        return self.customers.get(user_id)


    def get_jobs_by_customer(self,customer_id):
        if not isinstance(customer_id,str):
            raise TypeError("Customer id must be an instance of str")
        customer_id = customer_id.strip()
        if customer_id == "" :
            raise ValueError("Customer id cannot be an empty string")
        if customer_id not in self.customers:
            raise ValueError("Customer id not exists in customers")
        customer_jobs_list = []
        for job in list(self.jobs.values()):
            if job.customer_id == customer_id :
                customer_jobs_list.append(job)
        return customer_jobs_list


    def show_all_customers(self):
        return list(self.customers.values())




    def update_customer_address(self,customer_id,customer_address):
        updated_customer : Customer = self.find_customer(customer_id)
        if updated_customer is None:
            raise ValueError("Customer id not exists in customers")

        updated_customer.update_address(customer_address)



    def add_customer_notes(self,customer_id,new_notes):
        updated_customer : Customer = self.find_customer(customer_id)
        if updated_customer is None:
            raise ValueError("Customer id not exists in customers")
        updated_customer.add_notes(new_notes)


    def remove_customer_notes(self,customer_id):
        updated_customer : Customer = self.find_customer(customer_id)
        if updated_customer is None:
            raise ValueError("Customer id not exists in customers")
        updated_customer.remove_notes()


    def activate_customer(self,customer_id):
        customer : Customer = self.find_customer(customer_id)
        if customer is None:
            raise ValueError("Customer id not exists in customers")


        customer.active()



    def deactivate_customer(self,customer_id):
        customer : Customer = self.find_customer(customer_id)
        if customer is None:
            raise ValueError("Customer id not exists in customers")
        customer.inactive()





    ### providers ###



    def add_provider(self,provider):
        if not isinstance(provider,ServiceProvider):
            raise TypeError("Provider must be an instance of ServiceProvider")
        if provider.user_id in self.providers:
            raise ValueError("Provider id already exists in providers")
        if provider.user_id in self.customers:
            raise ValueError("provider id already exists in customers")
        self.providers[provider.user_id] = provider



    def find_provider(self,user_id):
        if not isinstance(user_id,str):
            raise TypeError("User id must be an instance of str")
        user_id = user_id.strip()
        if user_id == "" :
            raise ValueError("User id cannot be an empty string")
        if user_id not in self.providers:
            return None
        return self.providers.get(user_id)


    def get_jobs_by_provider(self,provider_id):
        if not isinstance(provider_id,str):
            raise TypeError("Provider id must be an instance of str")
        provider_id = provider_id.strip()
        if provider_id == "" :
            raise ValueError("Provider id cannot be an empty string")
        if provider_id not in self.providers:
            raise ValueError("Provider id not exists in providers")
        provider_jobs_list = []
        for job in self.jobs.values():
            if job.provider_id == provider_id :
                provider_jobs_list.append(job)
        return provider_jobs_list


    def show_all_providers(self):
        return list(self.providers.values())



    def update_provider_base_price(self,provider_id,new_base_price):
        provider : ServiceProvider = self.find_provider(provider_id)
        if provider is None:
            raise ValueError("Provider id not exists in providers")
        provider.update_base_price(new_base_price)



    def add_provider_profession(self, provider_id, new_profession):
        provider : ServiceProvider = self.find_provider(provider_id)
        if provider is None:
            raise ValueError("Provider id not exists in providers")
        provider.add_profession(new_profession)




    def mark_provider_availability(self,provider_id):
        provider : ServiceProvider = self.find_provider(provider_id)
        if provider is None:
            raise ValueError("Provider id not exists in providers")
        provider.mark_availability()





    def mark_provider_unavailability(self, provider_id):
        provider : ServiceProvider = self.find_provider(provider_id)
        if provider is None:
            raise ValueError("Provider id not exists in providers")
        provider.mark_unavailability()



    def activate_provider(self, provider_id):
        provider : ServiceProvider = self.find_provider(provider_id)
        if provider is None:
            raise ValueError("Provider id not exists in providers")
        provider.active()



    def deactivate_provider(self,provider_id):
        provider : ServiceProvider = self.find_provider(provider_id)
        if provider is None:
            raise ValueError("Provider id not exists in providers")
        provider.inactive()






    ### jobs ###


    def find_job(self,user_id):
        if not isinstance(user_id,str):
            raise TypeError("User id must be an instance of str")
        user_id = user_id.strip()
        if user_id == "" :
            raise ValueError("User id cannot be an empty string")
        if user_id not in self.jobs:
            return None
        return self.jobs.get(user_id)


    def create_job(self,customer_id,job_type,description,address,price):
        if not isinstance(customer_id,str):
            raise TypeError("Customer id must be an instance of str")
        customer_id = customer_id.strip()
        if customer_id == "" :
            raise ValueError("Customer id cannot be an empty string")
        if customer_id not in self.customers:
            raise ValueError("Customer id not exists in customers")
        job_id = f"job_{self.job_counter}"
        created_at = datetime.now()
        new_job = Job(job_id, customer_id, job_type, description, address, price, created_at)
        self.jobs[job_id] = new_job
        customer = self.customers[customer_id]
        customer.add_job_history(job_id)
        self.job_counter += 1
        return new_job


    def assign_provider_to_job(self,job_id,provider_id):
        if not isinstance(job_id,str):
            raise TypeError("Job id must be an instance of str")

        job_id = job_id.strip()
        if job_id == "" :
            raise ValueError("Job id cannot be an empty string")

        if job_id not in self.jobs:
            raise ValueError("Job id not exists in jobs")

        if not isinstance(provider_id,str):
            raise TypeError("Provider id must be an instance of str")

        provider_id = provider_id.strip()
        if provider_id == "" :
            raise ValueError("Provider id cannot be an empty string")

        if provider_id not in self.providers:
            raise ValueError("Provider id not exists in providers")

        this_job : Job = self.find_job(job_id)
        if this_job is None:
            raise ValueError("Job id not exists in jobs")

        if this_job.status != "open":
            raise ValueError("Job is not in status open")

        this_provider : ServiceProvider = self.find_provider(provider_id)
        if this_provider is None:
            raise ValueError("Provider id not exists in providers")

        if not  this_provider.is_active :
            raise ValueError("Provider id is not active")

        if not this_provider.availability :
            raise ValueError("Provider id is not available")

        if this_job.job_type not in this_provider.profession :
            raise ValueError("this provider not profession for this job")

        this_job.assign_provider(provider_id)



    def start_job(self,job_id):
        if not isinstance(job_id,str):
            raise TypeError("Job id must be an instance of str")
        job_id = job_id.strip()
        if job_id == "" :
            raise ValueError("Job id cannot be an empty string")
        if job_id not in self.jobs:
            raise ValueError("Job id not exists in jobs")
        this_job : Job = self.find_job(job_id)
        if this_job is None:
            raise ValueError("Job id not exists in jobs find method return None")
        if this_job.status != "assigned":
            raise ValueError("Job is not in status assigned")
        if not this_job.provider_id :
            raise ValueError(" provider id is not assigned for this job cannot start  ")
        this_job.start_job()



    def complete_job(self,job_id):
        if not isinstance(job_id,str):
            raise TypeError("Job id must be an instance of str")
        job_id = job_id.strip()
        if job_id == "" :
            raise ValueError("Job id cannot be an empty string")
        if job_id not in self.jobs:
            raise ValueError("Job id not exists in jobs")
        this_job: Job = self.find_job(job_id)
        if this_job is None:
            raise ValueError("Job id not exists in jobs find method return None")
        job_provider : ServiceProvider = self.find_provider(this_job.provider_id)
        if job_provider is None:
            raise ValueError(" provider id not exists in providers")
        this_job.complete_job()
        job_provider.add_completing_job(job_id)



    def cancel_job(self,job_id):
        if not isinstance(job_id,str):
            raise TypeError("Job id must be an instance of str")
        job_id = job_id.strip()
        if job_id == "" :
            raise ValueError("Job id cannot be an empty string")
        if job_id not in self.jobs:
            raise ValueError("Job id not exists in jobs")
        this_job : Job = self.find_job(job_id)
        if this_job is None:
            raise ValueError("Job id not exists in jobs find method return None")
        this_job.cancel_job()


    def get_jobs_by_status(self,status):
        if not isinstance(status,str):
            raise TypeError("status must be an instance of str")
        status = status.strip()
        if status == "":
            raise ValueError("status cannot be an empty string")
        if status not in StatusList:
            raise ValueError("status not in StatusList")
        list_jobs = list(self.jobs.values())
        list_status_jobs = []
        for job in list_jobs:
            if job.status == status:
                list_status_jobs.append(job)
        return list_status_jobs



    def get_all_jobs(self):
        return list(self.jobs.values())



    def update_job_price(self, job_id, new_price):
        job: Job = self.find_job(job_id)
        if job is None:
            raise ValueError("Job id not exists in jobs")
        job.update_price(new_price)



    def update_job_description(self, job_id, new_description):
        job: Job = self.find_job(job_id)
        if job is None:
            raise ValueError("Job id not exists in jobs")
        job.update_description(new_description)


    def update_job_address(self, job_id, new_address):
        job: Job = self.find_job(job_id)
        if job is None:
            raise ValueError("Job id not exists in jobs")
        job.update_address(new_address)


    def update_schedule_job (self, job_id, new_schedule):
        job: Job = self.find_job(job_id)
        if job is None:
            raise ValueError("Job id not exists in jobs")
        job.schedule_job(new_schedule)




    ### data ###

    def save_all_data(self):
        jobs_data=[]
        providers_data=[]
        customers_data=[]
        for customer in self.customers.values():
            customers_data.append(customer.to_dict())
        for job in self.jobs.values():
            jobs_data.append(job.to_dict())
        for provider in self.providers.values():
            providers_data.append(provider.to_dict())
        save_to_json("data/customers.json", customers_data)
        save_to_json("data/jobs.json", jobs_data)
        save_to_json("data/providers.json", providers_data)



    def load_all_data(self):
        self.customers={}
        self.providers = {}
        self.jobs={}
        customer_data=load_from_json("data/customers.json")
        providers_data=load_from_json("data/providers.json")
        jobs_data = load_from_json("data/jobs.json")
        for customer in customer_data:
            new_customer = Customer(
                customer["user_id"],
                customer["full_name"],
                customer["phone_number"],
                customer["email"],
                customer["city"],
                customer["address"],
                customer["job_history"],
                customer["notes"],
                customer["is_active"],
            )

            self.customers[new_customer.user_id] = new_customer

        for provider in providers_data:
            new_provider = ServiceProvider(
                provider["user_id"],
                provider["full_name"],
                provider["phone_number"],
                provider["email"],
                provider["city"],
                provider["profession"],
                provider["experience_years"],
                provider["base_price"],
                provider["completing_jobs"],
                provider["availability"],
                provider["is_active"],
            )
            self.providers[new_provider.user_id] = new_provider
        for job in jobs_data:
            created_at = datetime.fromisoformat(job["created_at"])

            if job["schedule_date"] is not None:
                schedule_date = datetime.fromisoformat(job["schedule_date"])
            else:
                schedule_date = None
            new_job = Job(
                job["job_id"],
                job["customer_id"],
                job["job_type"],
                job["description"],
                job["address"],
                job["price"],
                created_at,
                schedule_date,
                job["provider_id"],
                job["status"],

            )
            self.jobs[new_job.job_id] = new_job
        self.job_counter = len(self.jobs) + 1























































