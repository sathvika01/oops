# Define a base class Animal
class Animal:
    def sound(self):
        raise NotImplementedError("Subclass must implement abstract method")

# Define a subclass Dog
class Dog(Animal):
    def sound(self):
        return "Woof"

# Define a subclass Cat
class Cat(Animal):
    def sound(self):
        return "Meow"

# Create objects of Dog and Cat
dog = Dog()
cat = Cat()
print(dog.sound())  # Woof
print(cat.sound())  # Meow

