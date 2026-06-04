from models.User import User

class Customer(User):

    def __init__(self,user_id,full_name,phone_number,email,city,address,job_history = None,notes="",is_active=True):
        super().__init__(user_id,full_name,phone_number,email,city,is_active)

        if not isinstance(address,str):
            raise TypeError("Address must be a string")
        address = address.strip()
        if not address:
            raise ValueError("Address cannot be empty")

        if job_history is None:
            job_history = []
        if not isinstance(job_history,list):
            raise TypeError("Job history must be a list")
        for job in job_history:
            if not isinstance(job,str):
                raise TypeError("every Job in Job history must be a string")


        if not isinstance(notes,str):
            raise TypeError("Notes must be a string")
        notes = notes.strip()



        self.address = address
        self.job_history = job_history
        self.notes = notes



    def __str__(self):
        base = super().__str__()
        return (
            f"{base}\n"
            f"address: {self.address}\n"
            f"job_history: {self.job_history}\n"
            f"notes: {self.notes}"

        )

    def to_dict(self):
        base =  super().to_dict()
        base["address"] = self.address
        base["job_history"] = self.job_history
        base["notes"] = self.notes
        return base





    def add_job_history(self,new_job_id):
        if not isinstance(new_job_id,str):
            raise TypeError("new_job must be a string")
        new_job_id = new_job_id.strip()
        if not new_job_id:
            raise ValueError("new_job cannot be empty")
        self.job_history.append(new_job_id)


    def add_notes(self,new_notes):
        if not isinstance(new_notes,str):
            raise TypeError("new_notes must be a string")
        new_notes = new_notes.strip()
        if not new_notes:
            raise ValueError("new_notes cannot be empty")
        self.notes += "\n"
        self.notes += new_notes


    def remove_notes(self):
        self.notes = ""
        

    def update_address(self,new_address):
        if not isinstance(new_address,str):
            raise TypeError("new_address must be a string")
        new_address = new_address.strip()
        if not new_address:
            raise ValueError("new_address cannot be empty")
        self.address = new_address










