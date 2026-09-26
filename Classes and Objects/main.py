class Account():
    gender = ""
    username = ""
    password = ""
    age = 0
    email = "hello@gmail.com"
    phone_number = 0000000000

    #constructor
    def __init__(self):
        print("Creating a new account.")

    def details(self):
        self.gender = input("What is your gender?")
        self.age = int(input("Please say your age: "))
        self.username = input("What is your username?")
        self.password = input("Please create a password: ")
        self.email = input("(Optional) Please enter your email:")
        self.phone_number = int(input("Please enter your phone number: "))   

    def display_details(self):
        print("Are these your correct details?")
        print(self.gender)
        print(self.age)
        print(self.username)
        print(self.password)
        print(self.email)
        print(self.phone_number)

object = Account()
object.details()
object.display_details()