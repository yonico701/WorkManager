
class User:
    def __init__(self,user_id,full_name,phone_number,email,city,is_active = True):

      if not isinstance(user_id,str):
          raise TypeError('user_id must be a string')
      user_id = user_id.strip()
      if not user_id :
          raise ValueError('user_id cannot be empty')

      if not isinstance(full_name,str):
          raise TypeError('full_name must be a string')
      full_name = full_name.strip()
      if not full_name :
          raise ValueError('full_name cannot be empty')

      if not isinstance(phone_number,str):
          raise TypeError('phone_number must be a string')
      phone_number = phone_number.strip()
      if not phone_number.isdigit() or len(phone_number) != 10:
          raise ValueError('phone_number must be a numbers only and 10 digits allowed')

      if not isinstance(email,str):
          raise TypeError('email must be a string')
      email = email.strip()
      if "." not in email or "@" not in email:
          raise ValueError('email include "." and "@" ')


      if not isinstance(city,str):
          raise TypeError('city must be a string')
      city = city.strip()
      if not city:
          raise ValueError('city cannot be empty')

      if not isinstance(is_active,bool):
          raise TypeError('is_active must be a boolean')

      self.user_id = user_id
      self.full_name = full_name
      self.phone_number = phone_number
      self.email = email
      self.city = city
      self.is_active = is_active



    def __str__(self):
        status = "active" if self.is_active else "inactive"
        return (
          f"User ID: {self.user_id}\n"
          f"Full Name: {self.full_name}\n"
          f"Phone Number: {self.phone_number}\n"
          f"Email: {self.email}\n"
          f"City: {self.city}\n"
          f"Active: {status}"
        )

    def to_dict(self):
        return {
            'user_id' : self.user_id,
            'full_name' : self.full_name,
            'phone_number' : self.phone_number,
            'email' : self.email,
            'city' : self.city,
            'is_active' : self.is_active
        }


    def active(self):
        self.is_active = True

    def inactive(self):
        self.is_active = False

    










