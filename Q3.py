# 3. Explain the difference between instance methods and class methods. Provide an example of each.

# Example of an Instance Method:
class Dog:
    def __init__(self, name):
        self.name = name

    def bark(self):
        return f"{self.name} says woof!"

my_dog = Dog("Rex")
print(my_dog.bark()) 

# Example of a Class Method:
class Dog:
    species = "Canis lupus familiaris"

    def __init__(self, name):
        self.name = name

    @classmethod
    def get_species(cls):
        return cls.species

print(Dog.get_species())  

