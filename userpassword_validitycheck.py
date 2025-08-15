class UserInfo:
    def __init__ (self):
        self._username = []
        self._password = []


    def ask_input(self):
        self._username = input("Insert Username: ")
        self._password = input("Insert Password: ")


    def check_validity(self):
        username_check = "Ten" #when you know how you should make a list or even a json file where you iterate and find out if the username is valid
        password_check = "10"
        if (username_check == self._username) and (password_check == self._password):
            print("Valid")
        else:
            print ("Invalid")  
          
userlogin = UserInfo()
userlogin.ask_input()
userlogin.check_validity()