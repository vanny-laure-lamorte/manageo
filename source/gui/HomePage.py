import pygame
from source.pygame_manager.Element import Element
from source.Controller import Controller

class HomePage(Element, Controller):
    def __init__(self, user_info): 
        Element.__init__(self)
        Controller.__init__(self)
        self.user = user_info
        self.user_id, self.user_first_name, self.user_last_name, self.user_email = self.user[0], self.user[1], self.user[2], self.user[3]     

        # Error Message  
        self.accounts_running = True

        # Disconnect btn
        self.disconnected = True

        # Input
        self.entry = False

        # Main Page
        self.welcome_message = ""                   

        # Modify profile
        self.profile_modified = False

        #Load Image
        self.image_paths = {       
            "logout": "assets/image/MainPage/mainpage_off.png",
            "bell":"assets/image/MainPage/mainpage_bell.png",
            "background":"assets/image/MainPage/mainpage_background1.jpg",
            "profile":"assets/image/MainPage/mainpage_profile.png",
        }

        self.images = {}
        for name, path in self.image_paths.items():
            self.images[name] = pygame.image.load(path)

        self.profile_display= False
        self.confirm_button_rect, self.fname_input_rect, self.lname_input_rect, self.email_input_rect = pygame.Rect(0,0,0,0), pygame.Rect(0,0,0,0), pygame.Rect(0,0,0,0), pygame.Rect(0,0,0,0)

        self.welcome_message_list = ["Welcome to your profile! Here, you can view all the details and information pertinent to you",
        "Welcome! You are currently on the homepage where you can view your general details",
        "Welcome to your Product 1 !",
        "Welcome to your Product 2!",
        "Any issues, contact us. We would be happy to assist you!"
        ]

    def background(self):
        self.img_background(400, 300, 1244, 830, self.images["background"])

    def top_bar(self):

        # Rect
        self.rect_full(self.blue1, 500, 25, 1000, 30, 0)
        self.rect_full(self.blue2, 500, 75, 1000, 70, 0)
        self.rect_full(self.blue1, 500, 125, 1000, 30, 0)

        # Lines v top bar
        pygame.draw.line(self.Window, self.white, (850, 53), (850, 100), 1)
        pygame.draw.line(self.Window, self.white, (930, 53), (930, 100), 1)

        # Lines h top bar
        pygame.draw.line(self.Window, self.white, (0, 40), (1000, 40), 1)
        pygame.draw.line(self.Window, self.white, (0, 110), (1000, 110), 1)

        # Welcome message
        self.text_not_center(self.font1, 18, "Welcome Back to our Website", self.white, 10, 65)

        # Account ID Number
        self.text_not_center(self.font3, 13, " Your Account Number | XXXX ", self.white, 600, 75)

        # Notification Bell
        self.img_hover("bell", "bell", 890, 80, 40, 40,self.images["bell"],self.images["bell"])

        # Log Out Pic
        self.log_out_rect = self.img_hover("Log Out", "Log Out", 970, 80, 40, 40,self.images["logout"],self.images["logout"])

    def side_bar(self):

        # Rect Principale
        self.rect_full(self.grey, 140, 420, 250, 530, 5)
        self.rect_border(self.white, 140, 420, 250, 530, 2, 5)
        self.rect_radius_top(self.blue2, 140, 175, 250, 45, 5)

        # User info
        self.img_not_center("Profil pic", 90, 160, 90, 90, self.images["profile"])
        self.text_not_center(self.font1, 15, f"{self.user_first_name} {self.user_last_name}", self.grey3, 70, 260)
        self.profile_rect = self.button_hover_small("My Profil", 140, 310, 190, 40, self.blue2, self.blue2, self.blue2, self.blue2, "My Profil", self.font1, self.white,15, 0, 3)

        # Home Rect
        self.home_rect = self.button_hover_small("Home Page", 140, 360, 190, 40, self.blue2, self.blue2, self.blue2, self.blue2, "Home", self.font1, self.white,15, 0, 3 )

        # Lines h top bar
        pygame.draw.line(self.Window, self.grey3, (100, 405), (180, 405), 3)
        pygame.draw.line(self.Window, self.grey3, (100, 545), (180, 545), 3)

        # Product 1
        self.product1_rect = self.button_hover_small("My Product 1", 140, 450, 190, 40, self.blue2, self.blue2, self.blue2, self.blue2, "My Product 1", self.font1, self.white,15, 0, 3)

        # Product 2
        self.product2_rect = self.saving_rect = self.button_hover_small("My Product 2", 140, 500, 190, 40, self.blue2, self.blue2, self.blue2, self.blue2, "My Product 2", self.font1, self.white,15, 0, 3)

        # Contact Us
        self.contact_rect = self.button_hover_small("Contact Us", 140, 590, 190, 40, self.blue2, self.blue2, self.blue2, self.blue2, "Contact Us", self.font1, self.white,15, 0, 3)
    
    def main_section (self):

        # Main Rect in main section
        self.rect_full(self.grey, 630, 420, 700, 530, 5)
        self.rect_border(self.white, 630, 420, 700, 530, 2, 5)
        self.rect_radius_top(self.blue2, 630, 175, 700, 45, 5)

        # Welcome message
        self.text_not_center(self.font1, 14, self.welcome_message, self.white, 295, 170) 

    def default_page(self): 
        self.text_not_center(self.font1, 80,"Hi", self.blue2, 550, 350)
 
    def main_page_design(self):
        self.background()
        self.top_bar()
        self.side_bar()
        self.main_section()
    
    def profile_design(self):
      
        self.confirm_button_rect = self.button_hover_small("Confirm", 540, 520, 120, 30, self.blue2, self.blue2, self.blue2, self.blue2, "Confirm", self.font1, self.white,15, 0, 3)
        self.fname_input_rect = self.rect_full(self.white, 540, 310, 320, 30, 5)
        self.lname_input_rect = self.rect_full(self.white, 570, 360, 320, 30, 5) 
        self.email_input_rect = self.rect_full(self.white, 535, 410, 320, 30, 5) 

        self.text_not_center(self.font2, 12, "* Please click on the white rectangle to edit your information.", self.grey1, 300, 210)

        # Name
        self.text_not_center(self.font1, 16, "Name", self.grey1, 330, 300)
        self.text_not_center(self.font2, 16, self.user_first_name, self.grey1, 390, 300)
        pygame.draw.line(self.Window, self.green4, (330, 330), (750, 330), 1)

        # Surname
        self.text_not_center(self.font1, 16, "Surname", self.grey1, 330, 350)
        self.text_not_center(self.font2, 16,self.user_last_name, self.grey1, 420, 350)
        pygame.draw.line(self.Window, self.green4, (330, 380), (750, 380), 1)

        # Email
        self.text_not_center(self.font1, 16, "Email", self.grey1, 330, 400)
        self.text_not_center(self.font2, 16, self.user_email, self.grey1, 380, 400)
        pygame.draw.line(self.Window, self.green4, (330, 430), (750, 430), 1)

        if self.profile_modified:
            pygame.draw.line(self.Window, self.green, (615 - 6, 520 - 6), (615 + 2, 520 + 7), 3)
            pygame.draw.line(self.Window, self.green, (615 + 1, 520 + 7), (615 + 8, 520 - 12), 3)     
 

    def homepage_run(self):
       
        if self.accounts_running:
            self.background()
            self.side_bar()
            self.main_page_design()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pass

                

                if event.type == pygame.MOUSEBUTTONDOWN:
                   
                    if self.profile_rect.collidepoint(event.pos):
                        self.profile_display = True
                        self.welcome_message = self.welcome_message_list[0] 

                    elif self.product1_rect.collidepoint(event.pos):
                        pass
                    elif self.product2_rect.collidepoint(event.pos):
                        pass
                    elif self.contact_rect.collidepoint(event.pos):
                        pass

                    elif self.log_out_rect.collidepoint(event.pos):
                        self.disconnected = True
                        self.accounts_running = False          
                    
                    elif self.home_rect.collidepoint(event.pos):
                        self.profile_display = False
                        self.welcome_message = ""

                    elif self.confirm_button_rect.collidepoint(event.pos):
                        if (self.user_first_name not in ["Modify your first name", ""] and
                            self.user_last_name not in ["Modify your last name", ""] and
                            self.user_email not in ["Modify your email", ""]):
                            self.update_user(self.user_id, self.user_first_name, self.user_last_name, self.user_email)
                            self.profile_modified = True

                    # Modify profile
                    elif self.fname_input_rect.collidepoint(event.pos):
                        if self.user_first_name == "Modify your first name": 
                            self.user_first_name = ""
                        else:
                            self.user_first_name = "Modify your first name"
                        self.entry = 100                   

                    elif self.lname_input_rect.collidepoint(event.pos):
                        if self.user_last_name == "Modify your last name": 
                            self.user_last_name = ""
                        else:
                            self.user_last_name= "Modify your last name"
                        self.entry = 101

                    elif self.email_input_rect.collidepoint(event.pos):
                        if self.user_email== "Modify your email": 
                            self.user_email = ""
                        else:
                            self.user_email = "Modify your email"
                        self.entry = 102

                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_BACKSPACE:
                        if self.entry == 100: 
                            self.user_first_name = self.user_first_name[:-1]
                        elif self.entry == 101: 
                            self.user_last_name= self.user_last_name[:-1] 
                        elif self.entry == 102: 
                            self.user_email=  self.user_email[:-1] 

                    else:
                        if self.entry == 100:              
                            if event.unicode.isalpha():
                                self.user_first_name = self.user_first_name + event.unicode   

                        elif self.entry == 101:
                            if event.unicode.isalpha():
                                self.user_last_name= self.user_last_name + event.unicode                               

                        elif self.entry == 102:
                            if event.unicode.isalnum() or event.unicode in "@._-":
                                self.user_email = self.user_email + event.unicode   
                            
                    




               