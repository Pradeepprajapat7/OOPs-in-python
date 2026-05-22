class chatbook:
    def __init__(self):
        self.username = ""
        self.password = ""
        self.logging = False
        self.menu()
    
    def menu(self):
        user_input = input("""welcome to chatbook !!
                           1. press 1 for signup
                           2. press 2 for login
                           3. press 3 for post
                           4. press 4 send a message
                           5. press 5 for exit  """)
        if user_input == "1":
            self.signup()
        elif user_input == "2":
            self.signin()   
        elif user_input == "3":
            pass
        elif user_input == "4":
            pass
        else:
            exit()
    
    def signup(self):
        email = input("enter your email-->>")
        password = input("enter your password-->>")
        self.username = email
        self.password = password
        print("you are singup successfully! ")
        print("\n")
        self.menu()
    
    def signin(self):
        if self.username == "" and  self.password == "":
            print("you are not signup yet! ")
        else:
            uname = input("enter your email-->>")
            password = input("enter your password-->>") 
            if self.username == uname and self.password == password:
                print("you are login successfully! ")
                self.logging = True

            else:
                print("invalid username or password! ")
        print("\n")
        self.menu()

obj = chatbook()