my_list = [1, 2, 3]
my_set = set()

print(type(my_list))
print(type(my_set))


class Dog():
    def __init__(self, breed, name, spots):
        
        # Attributes
        # We take in the argument
        # Assign it using self.attribute_name

        self.breed = breed
        self.name = name
        # Expect boolean True / False
        self.spots = spots


my_dog = Dog(breed="Lab", name="Sammy", spots=False)
print(my_dog.breed)
print(my_dog.name)
print(my_dog.spots)


