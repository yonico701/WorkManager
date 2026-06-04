
from datetime import datetime
AllowJobTypes = ["plumbing","electricity","cleaning", "painting"]
StatusList = ["open", "assigned", "in_progress", "completed", "cancelled"]

class Job:
    def __init__(self, job_id,customer_id,job_type,description,address,price,created_at,schedule_date = None,provider_id = None,status = "open"):

        if not isinstance(job_id,str):
            raise TypeError("Job id must be a string")
        job_id = job_id.strip()
        if job_id == "":
            raise ValueError("Job id cannot be an empty string")

        if not isinstance(customer_id,str):
            raise TypeError("Job customer_id must be a string")
        customer_id = customer_id.strip()
        if customer_id == "":
            raise ValueError("Job customer_id cannot be an empty string")

        if not isinstance(job_type,str):
            raise TypeError("Job type must be a string")
        job_type = job_type.strip()
        if job_type not in AllowJobTypes:
            raise ValueError("Job type must be one of {}".format(AllowJobTypes))

        if not isinstance(description,str):
            raise TypeError("Job description must be a string")
        description = description.strip()
        if description == "":
            raise ValueError("Job description cannot be an empty string")

        if not isinstance(address,str):
            raise TypeError("Job address must be a string")
        address = address.strip()
        if address == "":
            raise ValueError("Job address cannot be an empty string")

        if not isinstance(price,(int,float)):
            raise TypeError("Job price must be a number")
        if price < 0:
            raise ValueError("Job price cannot be negative")

        if not isinstance(created_at,datetime):
            raise TypeError("Job created_at must be a datetime")

        if not schedule_date is None:
            if not isinstance(schedule_date,datetime):
                raise TypeError("Job schedule_date must be a datetime")

        if not isinstance(status,str):
            raise TypeError("Job status must be a string")
        status = status.strip()
        if status=="":
            raise ValueError("Job status cannot be an empty string")
        if status not in StatusList:
            raise ValueError("Job status must be one of {}".format(StatusList))


        if not provider_id is None:
            if not isinstance(provider_id,str):
                raise TypeError("Job provider_id must be a string")
            provider_id = provider_id.strip()
            if provider_id == "":
                raise ValueError("Job provider_id cannot be an empty string")



        if status in ["assigned","in_progress","completed"] and provider_id is None:
            raise ValueError("Job status cannot be assigned or in_progress without provider id")


        self.job_id = job_id
        self.customer_id = customer_id
        self.job_type = job_type
        self.description = description
        self.address = address
        self.price = price
        self.created_at = created_at
        self.schedule_date = schedule_date
        self.provider_id = provider_id
        self.status = status


    def __str__(self):
        return (
            f"job_id:{self.job_id}\n"
            f"customer_id:{self.customer_id}\n"
            f"job_type:{self.job_type}\n"
            f"description:{self.description}\n"
            f"address:{self.address}\n"
            f"price:{self.price}\n"
            f"created_at:{self.created_at}\n"
            f"schedule_date:{self.schedule_date}\n"
            f"provider_id:{self.provider_id}\n"
            f"status:{self.status}\n"

        )

    def to_dict(self):
        return {
            'job_id': self.job_id,
            'customer_id': self.customer_id,
            'job_type': self.job_type,
            'description': self.description,
            'address': self.address,
            'price': self.price,
            'created_at': self.created_at.isoformat(),
            'schedule_date': self.schedule_date.isoformat() if self.schedule_date else None,
            'provider_id': self.provider_id,
            'status': self.status,

        }

    def assign_provider(self,provider_id):
        if not isinstance(provider_id,str):
            raise TypeError("provider_id must be a string")
        provider_id = provider_id.strip()
        if provider_id == "":
            raise ValueError(" provider_id cannot be an empty string")
        self.provider_id = provider_id
        self.status = "assigned"


    def start_job(self):
        if self.provider_id is None:
            raise ValueError(" provider_id cannot be null")

        if self.status != "assigned":
           raise ValueError("Job status must be assigned")

        self.status = "in_progress"

    def complete_job(self):
        if self.provider_id is None:
            raise ValueError("provider_id cannot be null")
        if self.status != "in_progress":
            raise ValueError("Job status must be in_progress")

        self.status = "completed"

    def cancel_job(self):
           if self.status == "completed":
               raise ValueError("Job status is already completed and cannot be cancelled")
           if self.status == "cancelled":
               raise ValueError("Job status is already cancelled")
           self.status = "cancelled"





    def schedule_job(self,new_schedule_date):
        if not isinstance(new_schedule_date,datetime):
            raise TypeError("New schedule date must be a datetime")
        if self.status in ["completed","cancelled" , "in_progress"]:
            raise ValueError("Job status must be assigned or open to schedule Job")
        if new_schedule_date < datetime.now():
            raise ValueError("New schedule date cannot be in the past")

        self.schedule_date = new_schedule_date


    def update_price(self,new_price):
        if not isinstance(new_price,(int,float)):
            raise TypeError("New price must be a number")
        if new_price <= 0:
            raise ValueError("New price cannot be negative")
        self.price = new_price

    def update_description(self,new_description):
        if not isinstance(new_description,(str,)):
            raise TypeError("New description must be a string")
        new_description = new_description.strip()
        if new_description == "":
            raise ValueError("New description cannot be an empty string")
        self.description = new_description


    def update_address(self,new_address):
        if not isinstance(new_address,(str,)):
            raise TypeError("New address must be a string")
        new_address = new_address.strip()
        if new_address == "":
            raise ValueError("New address cannot be an empty string")
        self.address = new_address




























