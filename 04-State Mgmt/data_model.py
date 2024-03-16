from enum import Enum

class EnumUser(Enum):   
    """Enum class for user input states.""" 
    NAME=1
    EMAIL=2
    PHONE=3
    DONE=4

class ConState:
    """Class to keep track of the current state of user input."""

    def __init__(self):
        self.profile = EnumUser.NAME
    @property
    def CurrentPos(self):
        return self.profile
    @CurrentPos.setter
    def EnumUser(self,current:EnumUser):
        self.profile = current

class UserProfile:
    """ Class to represent the user profile. """
    def __init__(self):
        self.name = ""
        self.email=""
        self.phone=""

    @property
    def Name(self):
        return self.name
    @Name.setter
    def Name(self,name:str):
        self.name = name
    
    @property
    def Email(self):
        return self.email
    @Email.setter
    def Email(self,email:str):
        self.email = email

    @property
    def Phone(self):
        return self.phone
    @Phone.setter
    def Phone(self,phone:str):
        self.phone = phone