class Human:
    age = int
    first_name = str
    last_name = str
    weight = int

    def __init__(self, first_name, last_name, age, weight=0):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.weight = weight

    def info(self):
        print(f"I'm {self.first_name}, age: {self.age}, weight: {self.weight}")


john = Human("John", "Man", 30)
arthur = Human("Arthur", "None", 40)
#
# print(john, arthur)
#
# john.age = 30
# john.first_name = "John"
# john.last_name = "Lastok1"
# arthur.age = 40
# arthur.first_name = "Arthur"
# arthur.last_name = "Lastok2"

print(john.first_name, john.last_name, john.age, john.weight)
print(arthur.first_name, arthur.last_name, arthur.age, arthur.weight)
arthur.info()
john.info()
