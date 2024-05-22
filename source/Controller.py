from hashlib import sha256
from data.UserRepository import UserRepository

class Controller(UserRepository):

    def __init__(self):
        UserRepository.__init__(self)

        # Home
        self.input_email = ""
        self.input_password = ""

        # Signup
        self.input_first_name_register = ""
        self.input_last_name_register = ""
        self.input_email_register = ""
        self.input_password_register = ""     

        # Link pages 
        self.register = False
        self.connected = False

    # Check Password and email to allow account access
    def login_user(self):
        hashed_password = sha256(self.input_password.encode()).hexdigest()

        if self.check_credentials(self.input_email, hashed_password):
            self.user = self.get_user(self.input_email, hashed_password)
            self.connected = True
            return self.user
        
    # Collect info of a new user
    def register_user(self):
        hashed_password_register = sha256(self.input_password_register.encode()).hexdigest()
        self.new_user = self.add_user(self.input_first_name_register, self.input_last_name_register, self.input_email_register, hashed_password_register)
        return self.new_user
        