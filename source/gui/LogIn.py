import pygame, random, webbrowser
from source.pygame_manager.Element import Element
from source.pygame_manager.Animation import Animation
from source.Controller import Controller
from source.gui.HomePage import HomePage

class LogIn(Element, Animation, Controller):
    def __init__(self):
        Element.__init__(self)
        Animation.__init__(self)
        Controller.__init__(self)

        self.login_running = True
        self.register_running = False
        self.quit = False

        # Error Message
        self.error_login = False
        self.error_fn = False
        self.error_ln = False
        self.error_em = False
        self.error_pw = False
        self.error_op = False
        self.error_ck = False

        self.entry = False
        self.running = True

        self.checkbox = False


        # Password
        self.show_pass = False
        self.password_display = " *" * len(self.input_password)

        # Load Images
        self.image_paths = {
            "twitter": "assets/image/LogIn/login_twitter.png",
            "instagram": "assets/image/LogIn/login_instagram.png",
            "facebook": "assets/image/LogIn/login_facebook.png",
            "background": "assets/image/LogIn/background_m.png",
            "eye":"assets/image/LogIn/login_eye.png",
            "logoManageo": "assets/image/LogIn/logoManageo.png"
        }

        self.images = {}
        for name, path in self.image_paths.items():
            self.images[name] = pygame.image.load(path)


    def validate_password(self, password):
        has_special = any(char in '!@#$%^&*()-_+=~`[]{}|\\:;"<>,.?/' for char in password)
        has_digit = any(char.isdigit() for char in password)
        has_upper = any(char.isupper() for char in password)
        return has_special and has_digit and has_upper and len(password) >= 8

    def validate_email(self, email):
        return '@' in email and '.' in email

    def gui_home(self):

        # Background
        self.img_background(400, 300, 1244, 830, self.images["background"])

        # Logo Manageo 
        self.img_not_center("Logo Manageo", 50, 100, 500, 500, self.images["logoManageo"])

        # Rect principal
        self.rect_full(self.blue1, self.W//2+220, self.H//2, 400, 580, 10)
        self.rect_border(self.white, self.W//2+220, self.H//2, 400, 580, 1, 10)

        # Login Welcome Back Message
        self.text_center(self.font1, 35, "Log In", self.white, self.W//2+220, 140)
        self.text_center(self.font4, 16, "Welcome back to our website !", self.white, self.W//2+220, 180)

        # Email
        self.input_email_rect = self.button_hover("Email", self.W//2+220, 250, 350, 50, self.blue2, self.blue2, self.blue2, self.green2, self.input_email, self.font4, self.white,18, 1, 5)
        self.text_input(self.input_email_rect, self.input_email, "Email address", 720, 250, 350, 50, id="email_login")

        # Password
        self.input_password_rect = self.button_hover("Password", self.W//2+220, 320, 350, 50, self.blue2, self.blue2, self.blue2, self.green2, self.password_display, self.font4, self.white, 18, 1, 5)
        self.text_input(self.input_password_rect, self.password_display, "Password", 720, 320, 350, 50, id="email_login")

        # Eye
        self.img_background(870, 320, 25, 25, self.images["eye"])
        self.show_pass_rect = pygame.Rect(858, 310, 25, 25)
        
        if self.show_pass:
           self.password_display = self.input_password
        else:
            self.password_display = " *" * len(self.input_password)            

        # Login
        self.login_rect = self.button_hover("Login", self.W//2+220, 390, 350, 50, self.blue2, self.blue2, self.blue2, self.blue2,"Log In", self.font1, self.white, 18, 1, 5) 
     
        # Error message
        if self.error_login:
            self.text_center(self.font1, 16, "Wrong Email or Password", self.red, 720, 430)

        # No Account
        self.text_center(self.font1, 13, "No account ?", self.white, self.W//2+190, 450)
        self.text_center(self.font4, 13, "Create one!", self.white, self.W//2+265, 450)

        # Lines
        pygame.draw.line(self.Window, self.white, (550, 450), (640, 450), 1)
        pygame.draw.line(self.Window, self.white, (805, 450), (895, 450), 1)
        pygame.draw.line(self.Window, self.white, (520, 575), (919, 575), 1)

        # Social Media
        self.img_hover("Twitter", "Twitter", self.W//2+160, 610, 35, 35,self.images["twitter"],self.images["twitter"])
        self.img_hover("Instagram", "Instagram", self.W//2+220, 610, 35, 35,self.images["instagram"],self.images["instagram"])
        self.img_hover("Facebook", "Facebook", self.W//2+280, 610, 35, 35, self.images["facebook"], self.images["facebook"])

        # Sign In
        self.signup_rect = pygame.draw.rect(self.Window, self.blue1, [675, 490, 90, 20])
        self.sign = (pygame.Rect(675, 490, 90, 20))
        if self.is_mouse_over_button(self.sign):
            self.text_center(self.font4, 15, "Sign-in options", self.white, self.W//2+220, 500)
        else:
            self.text_center(self.font4, 13, "Sign-in options", self.white, self.W//2+220, 500)

    def gui_register(self):

        self.screen_color(self.white)

        # Background
        self.img_background(400, 300, 1244, 830, self.images["background"])

        # Rect principal
        self.rect_full(self.blue2, self.W//2, self.H//2, 950, 650, 5)
        self.rect_border(self.white, self.W//2, self.H//2, 950, 650, 1, 10)

        # About you
        self.text_center(self.font4, 25, "About you", self.white, self.W//2, self.H//2-270)

        if self.error_fn:
            self.text_center(self.font4, 15, "Invalid Input", self.red, self.W//2, self.H//2-232)

        # First Name
        self.input_first_name_register_rect = self.button_hover("", self.W//2, self.H//2-192, 350, 50, self.blue2, self.blue1, self.blue2, self.blue1, self.input_first_name_register, self.font4, self.white,15, 1, 5)
        self.text_center(self.font4, 15, "First Name", self.white, self.W//2, self.H//2-232)

        if self.error_ln:
            self.text_center(self.font4, 15, "Invalid Input", self.black, self.W//2, self.H//2-147)

        # Last Name
        self.input_last_name_register_rect = self.button_hover("", self.W//2, self.H//2-107, 350, 50, self.blue2, self.blue1, self.blue2, self.blue1, self.input_last_name_register, self.font4, self.white,15, 1, 5)
        self.text_center(self.font4, 15, "Last Name", self.white, self.W//2, self.H//2-147)

        # Email
        self.input_email_register_rect = self.button_hover("", self.W//2, self.H//2-22, 350, 50, self.blue2, self.blue1, self.blue2, self.blue1, self.input_email_register, self.font4, self.white,15, 1, 5)
        self.text_center(self.font4, 15, "Email", self.white, self.W//2, self.H//2-62)

        if self.error_em:
            self.text_center(self.font4, 15, "Invalid Input", self.red, self.W//2, self.H//2-62)
            self.text_center(self.font4, 15, "example@example.com", self.red, self.W//2, self.H//2-22)
        if self.error_pw:
            self.text_center(self.font4, 15, "Invalid Input", self.red, self.W//2, self.H//2+17)
            self.text_center(self.font4, 15, "Password should have ", self.red, self.W//2, self.H//2+95)
            self.text_center(self.font4, 13, "- Minimum of 8 Characters", self.red, self.W//2, self.H//2+95)
            self.text_center(self.font4, 13, "- Lower cases letters", self.red, self.W//2, self.H//2+108)
            self.text_center(self.font4, 13, "- Upper cases letters", self.red, self.W//2, self.H//2+122)
            self.text_center(self.font4, 13, "- Numbers", self.red, self.W//2, self.H//2+134)
            self.text_center(self.font4, 13, "- Special Character", self.red, self.W//2, self.H//2+147)

        # Password
        self.input_password_register_rect = self.button_hover("", self.W//2, self.H//2+57, 350, 50, self.blue2, self.blue1, self.blue2, self.blue1, self.input_password_register, self.font4, self.white, 15, 1, 5)
        self.text_center(self.font4, 15, "Password", self.white, self.W//2, self.H//2+17)
   
        # Terms & conditions
        self.checkbox_rect_rect = self.rect_full(self.blue1, self.W//2, self.H//2+220, 500, 25, 2)
        self.text_center(self.font4, 17, "I agree to Manageo's terms and conditions", self.white, self.W//2, self.H//2+220)
        self.checkbox_rect = self.rect_full(self.white, self.W//2-220, self.H//2+220, 15, 15, 2)

        # Register button
        self.register_rect = self.button_hover("Register", self.W//2, self.H//2+270, 350, 50, self.blue1, self.blue1, self.blue1, self.blue1,"Register", self.font4, self.white, 19, 1, 5)

        if self.error_ck:
            self.text_center(self.font4, 15, "Checkbox Required", self.red, self.W//2+360, self.H//2+220)

        # Draw Checkbox Lines if checkbox TRUE
        if self.checkbox:
            pygame.draw.line(self.Window, self.green, (self.W//2 - 220 - 6, self.H//2 + 220 - 6), (self.W//2 - 220 + 2, self.H//2 + 220 + 7), 3)
            pygame.draw.line(self.Window, self.green, (self.W//2 - 220 + 1, self.H//2 + 220 + 7), (self.W//2 - 220 + 8, self.H//2 + 220 - 12), 3)      

    def login_run(self):
        if self.login_running:
            self.gui_home()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.quit = True
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if self.input_email_rect.collidepoint(event.pos):
                        self.entry = 1

                    elif self.show_pass_rect.collidepoint(event.pos):
                        self.show_pass = True                  

                    elif self.input_password_rect.collidepoint(event.pos):
                        self.entry = 2

                    elif self.login_rect.collidepoint(event.pos):
                        self.user = self.login_user()
                        if self.user != None:
                            self.login_running = False
                        else:
                            self.error_login = True

                    elif self.signup_rect.collidepoint(event.pos):
                        self.register_running = True
                        self.login_running = False             
                   
                elif event.type == pygame.MOUSEBUTTONUP:
                    if self.show_pass_rect.collidepoint(event.pos):
                        self.show_pass = False

                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_BACKSPACE:
                        if self.entry == 1:
                            self.input_email = self.input_email[:-1]
                        elif self.entry == 2:
                            self.input_password = self.input_password[:-1]
                    else:
                        if self.entry == 1:
                            self.input_email += event.unicode
                            self.error_login = False

                        elif self.entry == 2:
                            self.input_password += event.unicode
                            self.error_login = False           

    def register_run(self):
        if self.register_running:
            self.gui_register()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.quit = True

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.input_first_name_register_rect.collidepoint(event.pos):
                        self.error_fn = False
                        self.entry = 3

                    elif self.input_last_name_register_rect.collidepoint(event.pos):
                        self.error_ln = False
                        self.entry = 4

                    elif self.input_email_register_rect.collidepoint(event.pos):                
                        self.error_em = False
                        self.entry = 5

                    elif self.input_password_register_rect.collidepoint(event.pos):
                        self.error_pw = False
                        self.entry = 6                  

                    elif self.register_rect.collidepoint(event.pos):
                        if (not self.input_first_name_register or
                            not self.input_last_name_register or
                            not self.input_email_register or
                            not self.input_password_register or                       
                            not self.checkbox):
                            if self.input_first_name_register == "":
                                self.error_fn = True
                            if self.input_last_name_register == "":
                                self.error_ln = True
                            if self.input_email_register == "" or not self.validate_email(self.input_email_register):
                                self.error_em = True
                            if self.input_password_register == ""  or not self.validate_password(self.input_password_register):
                                self.error_pw = True                           
                            if not self.checkbox:
                                self.error_ck = True
                        else:                       
                            self.register_user()
                            self.login_running = True
                            self.register_running = False
                            self.checkbox = False                         
                            self.input_first_name_register = ""
                            self.input_last_name_register = ""
                            self.input_email_register = ""                    

                    elif self.checkbox_rect.collidepoint(event.pos):
                        self.checkbox = not self.checkbox
                        self.error_ck = False
                        self.account_details()
                        pass

                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_BACKSPACE:
                        if self.entry == 3:
                            self.input_first_name_register = self.input_first_name_register[:-1]
                        elif self.entry == 4:
                            self.input_last_name_register = self.input_last_name_register[:-1]
                        elif self.entry == 5:
                            self.input_email_register = self.input_email_register[:-1]
                        elif self.entry == 6:
                            self.input_password_register = self.input_password_register[:-1]
                    else:
                        if self.entry == 3 and len(self.input_first_name_register) < 14:
                            self.input_first_name_register += event.unicode

                        elif self.entry == 4 and len(self.input_last_name_register) < 14:
                            self.input_last_name_register += event.unicode

                        elif self.entry == 5 and len(self.input_email_register) < 32:
                            self.input_email_register +=  event.unicode

                        elif self.entry == 6 and len(self.input_password_register) < 32:
                            self.input_password_register += event.unicode