#1. Class attributes vs Instance Attributes
"""
Define a class BankAccount with a class attribute bank_name and instance attributes account_holder and balance.
Create two objects and print the class and instance attributes for each object.
"""

class BankAccount:
    bank_name = "SBI"
    def __init__(self,account_holder,balance):
        self.account_holder = account_holder
        self.balance = balance

account1 = BankAccount("Sathu",12345)
print(f"{account1.account_holder},{account1.balance},{account1.bank_name}")

"""
2. Encapsulation with Private Attributes
Create a class Employee with private attributes name and salary. Provide getter and setter methods for both attributes. 
Create an object and test the encapsulation by accessing and modifying the private attributes through the methods.
"""
class Employee:
    def __init__(self,name,salary):
        self.__name = name
        self.__salary = salary

    def get_name(self):
        return self.__name
    def set_name(self,name):
        self.__name=name
    def get_salary(self):
        return self.__salary
    def set_salary(self,salary):
        self.__salary = salary

e1 = Employee("sathu",20000)
print(e1.get_name())
e1.set_salary(30000)
print(e1.get_salary())

"""
3. Inheritance
Define a class Vehicle with attributes make and model. Create a subclass Car that adds the attribute number_of_doors. 
Instantiate an object of Car and print all its attributes.
"""
class Vehicle:
    def __init__(self,make,model):
        self.make = make
        self.model = model

class Car(Vehicle):
    def __init__(self,make,model,number_of_doors):
        super().__init__(make,model)
        self.number_of_doors = number_of_doors
car = Car("Toyota","Camry",4)
print(f"Make: {car.make}, Model:{car.model}, Doors:{car.number_of_doors}")

"""
4.Method Overriding
Create a class Bird with a method fly. Create a subclass Penguin that overrides the fly method to print "Penguins cannot 
fly". Instantiate objects of both classes and call the fly method on each.
"""
class Bird:
    def fly(self):
        return f"Birds fly"
class Penguin(Bird):
    def fly(self):
        return f"Penguins cannot fly!"

b1 = Bird()
print(b1.fly())
p1 = Penguin()
print(p1.fly())

"""
5.Polymorphism with Method Overriding
Define a base class Instrument with a method play. 
Create two subclasses Guitar and Piano that override the play method to print different messages. 
Create a list of Instrument objects and call the play method on each object in a loop.
"""
class Instrument:
    def play(self):
        raise NotImplementedError("Subclass must implemnet abstract method")
class Guitar(Instrument):
    def play(self):
        return f"I'm Guitarist"
class Piano(Instrument):
    def play(self):
        return f"I play Piano"

instruments = [Guitar(),Piano()]
for instrument in instruments:
    print(instrument.play())

"""
6.Composition
Create two classes Engine and Car. The Engine class should have an attribute horsepower. 
The Car class should have an attribute engine (an instance of the Engine class). Create an object of Car and print the 
horsepower of its engine.
"""
class Engine:
    def __init__(self,horsepower):
        self.horsepower = horsepower
class Car:
    def __init__(self,engine):
        self.engine = engine

my_engine = Engine(3000)
my_car = Car(my_engine)
print(f"The car's engine has {my_car.engine.horsepower} horsepower")
"""
7.Class Method and Static Method
Create a class Temperature with a static method celsius_to_fahrenheit and a class method from_fahrenheit. The static 
method should convert Celsius to Fahrenheit, and the class method should create a Temperature object from a Fahrenheit value.
"""
class Temperature:
    @staticmethod
    def celsius_to_fahrenheit(celsius):
        return (celsius * 9/5) + 32
    @classmethod
    def from_fahrenheit(cls, fahrenheit):
        celsius = (fahrenheit - 32)*5/9
        return cls(celsius)
    def __init__(self,celsius):
        self.celsius = celsius
temp = Temperature(25)
print(f"25 Celsius in Fahrenheit is {Temperature.celsius_to_fahrenheit(25)}")

"""
8.Dunder Methods

Define a class Vector with attributes x and y. Implement the __add__ method to add two vectors. 
Create two Vector objects and use the + operator to add them
"""
class Vector:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def __add__(self, other):
        return Vector(self.x + other.x, self.y+other.y)
    def __str__(self):
        return f"Vector({self.x},{self.y})"

vector1 = Vector(2,3)
vector2 = Vector(5,8)

result = vector1 + vector2
print(result)





