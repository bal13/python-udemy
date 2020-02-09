class Dog:
    # CLASS OBJECT ATTRIBUTE
    # SAME FOR ANY INSTANCE OF THE CLASS
    species = "mammal"

    def __init__(self, breed, name):
        # Attributes
        # We take in the argument
        # Assign it using self.attribute_name

        self.breed = breed
        self.name = name

    # OPERATIONS/Actions ---> Methods
    def bark(self, number):
        print(f"WOOF! My name is {self.name} and the number is {number}")


my_dog = Dog("Lab", "Frankie")

print(my_dog.breed)
print(my_dog.name)
print(my_dog.species)

my_dog.bark(10)


class Circle:
    # CLASS OBJECT ATTRIBUTE
    pi = 3.14

    def __init__(self, radius = 1):
        self.radius = radius
        self.area = radius * radius * Circle.pi # self.pi helyett ezt is lehet, ha class object attribute amire
                                                # hivatkozunk

    # METHOD
    def circumference(self):
        return self.radius * self.pi * 2


my_circle = Circle(30)
print(my_circle.pi)
print(my_circle.radius)
print(my_circle.circumference())
print(my_circle.area)