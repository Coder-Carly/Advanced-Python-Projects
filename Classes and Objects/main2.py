class Animal():
    animal_name = ""
    animal_sound = ""

    def __init__(self):
        print("Logging new animal sound")

    def animal(self):
        self.animal_name = input("Please enter the animal's name: ")
        self.animal_sound = input("Please enter the sound it makes: ")

    def display_animal(self):
        print("New animal logged: ")
        print(self.animal_name)
        print(self.animal_sound)

object = Animal()
object.animal()
object.display_animal()