my_list = [1, 2, 3]
my_set = set()

print(type(my_list))
print(type(my_set))


class Dog():
    def __init__(self, breed):
        self.breed = breed


my_dog = Dog(breed="Lab")
print(type(my_dog))

print(my_dog.breed)
