class Car():
    brand = ""
    speed = 0

    def __init__(self):
        print("Logging new car: ")

    def details(self):
        self.brand = input("Please enter your car brand: ")
        self.speed = int(input("Enter the speed of your car: "))

    def accelerate(self):
        self.speed += 10

    def display_details(self):
        print("Logging new car details: ")
        print(self.brand)
        print(self.speed)

car = Car()
car.details()
car.accelerate()
car.accelerate()
car.display_details()