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
            pass
        elif user_input == "2":
            pass    
        elif user_input == "3":
            pass
        elif user_input == "4":
            pass
        elif user_input == "5":
            print("thank you for using chatbook")

obj = chatbook()