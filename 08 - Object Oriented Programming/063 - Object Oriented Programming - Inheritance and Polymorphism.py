class Animal():
    def __init__(self):
        print("ANIMAL CREATED")

    def who_am_i(self):
        print("I am an animal")

    def eat(self):
        print("I am eating")


class Dog(Animal):
    def __init__(self):
        Animal.__init__(self)
        print("DOG CREATED")

    def who_am_i(self):
        print("I am a dog")

    def bark(self):
        print("WOOF")

    def eat(self):
        print("I am a dog eating")


my_animal = Animal()
my_animal.eat()
my_animal.who_am_i()
my_dog = Dog()
my_dog.eat()
my_dog.who_am_i()
my_dog.bark()


# Polymorphism
class Dog():

    def __init__(self, name):
        self.name = name

    def speak(self):
        return self.name + " says woof!"


class Cat():

    def __init__(self, name):
        self.name = name

    def speak(self):
        return self.name + " says meow!"


niko = Dog("Niko")
felix = Cat("Felix")
print(niko.speak())
print(felix.speak())

# 1
for pet in [niko, felix]:
    print(type(pet))
    print(pet.speak())


# 2
def pet_speak(pet):
    print(pet.speak())


pet_speak(niko)
pet_speak(felix)


class Animal():
    def __init__(self, name):
        self.name = name

    def speak(self):
        raise NotImplementedError("Subclass must implement this abstract method")


# my_animal = Animal("Fred")
# my_animal.speak()

class Dog(Animal):
    def speak(self):
        return self.name + " says woofff"


class Cat(Animal):
    def speak(self):
        return self.name + " says meoooowwww"


my_cat = Cat("Cicc")
my_dog = Dog("Woff")
print(my_cat.speak())
print(my_dog.speak())