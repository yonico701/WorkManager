from models.Job import AllowJobTypes
from models.User import User




class ServiceProvider(User):
    def __init__(self, user_id,
                 full_name,
                 phone_number,
                 email,
                 city,
                 profession,
                 experience_years,
                 base_price,
                 completing_jobs=None,
                 availability=True,
                 is_active=True
                 ):
        super().__init__(user_id,full_name,phone_number,email,city,is_active)

        if not isinstance(experience_years,int):
            raise TypeError("experience_years must be an integer")
        if experience_years < 0:
            raise ValueError("experience_years must be >= 0")

        if not isinstance(base_price,(int,float)):
            raise TypeError("base_price must be a float or integer")
        if base_price < 0:
            raise ValueError("base_price must be >= 0")

        if completing_jobs is None :
            completing_jobs = []
        if not isinstance(completing_jobs,list):
            raise TypeError("completing_jobs must be a list")
        for job in completing_jobs:
            if not isinstance(job,str):
                raise TypeError("completing_jobs must be a string")
            if not job.strip():
                raise ValueError("completing_jobs cannot be an empty string")



        if not isinstance(availability,bool):
            raise TypeError("availability must be a boolean")


        if not isinstance(profession,list):
            raise TypeError("profession must be a list")
        if not profession:
            raise ValueError("profession cannot be an empty list")
        for prof in profession:
            if not isinstance(prof,str):
                raise TypeError("profession must be a string")
            prof = prof.strip()
            if prof == "":
                raise ValueError("profession cannot be an empty string")
            if prof not in AllowJobTypes:
                raise ValueError("one or more professions not allowed")







        self.availability = availability
        self.profession = profession
        self.completing_jobs = completing_jobs
        self.experience_years = experience_years
        self.base_price = base_price


    def __str__(self):
        base = super().__str__()
        return (
            f"{base}\n"
            f"profession: {self.profession}\n"
            f"completing_jobs: {self.completing_jobs}\n"
            f"experience_years: {self.experience_years}\n"
            f"base_price: {self.base_price}\n"
            f"availability: {self.availability}\n"

        )

    def to_dict(self):
        base = super().to_dict()
        base["profession"] = self.profession
        base["completing_jobs"] = self.completing_jobs
        base["experience_years"] = self.experience_years
        base["base_price"] = self.base_price
        base["availability"] = self.availability
        return base


    def add_profession(self,new_profession):
        if not isinstance(new_profession,str):
            raise TypeError("profession must be a string")
        new_profession = new_profession.strip()
        if new_profession == "" :
            raise ValueError("profession cannot be an empty string")
        if new_profession not in AllowJobTypes:
            raise ValueError(f"profession must be one of: {AllowJobTypes}")
        if new_profession in self.profession:
            raise ValueError(" profession already exists")
        self.profession.append(new_profession)

    def update_base_price(self,new_base_price):
        if not isinstance(new_base_price,(int,float)):
            raise TypeError("base_price must be a float or integer")
        if new_base_price < 0:
            raise ValueError("base_price must be >= 0")
        self.base_price = new_base_price

    def add_completing_job(self,new_completing_job):
        if not isinstance(new_completing_job,str):
            raise TypeError("completing_jobs must be a string")
        new_completing_job = new_completing_job.strip()
        if new_completing_job == "" :
            raise ValueError("completing_jobs cannot be an empty string")
        self.completing_jobs.append(new_completing_job)


    def mark_unavailability(self):
        self.availability = False

    def mark_availability(self):
        self.availability = True


