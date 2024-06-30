#from typing import Self
from datetime import date
class Calculator:
    def __init__(self, version: int):
        self.version = version
    def description(self):
        print(f"Curently running Calculator on version: {self.version}")
    #these static methods can be placed anywhere in the code as per user convinence inside or
    #outside the class you can call them with or without instance variables
    #staticmethods donot change class values
    @staticmethod
    def add_numbers(self, *numbers: float):
        return sum(numbers)

calc1 = Calculator(10)
calc2 = Calculator(200)

calc1.description()
calc2.description()
print(Calculator.add_numbers(10,20,30))
print(calc1.add_numbers(10,20,30))

class Person:
    def __init__(self, name:str, age:int):
        self.name = name
        self.age = age
    def description(self):
        return f"{self.name} is {self.age} years old"
    #classmethods change the original values
    @classmethod
    def age_from_year(cls, name:str, birth_year: int):
        current_year: int = date.today().year
        age: int = current_year - birth_year
        return cls(name,age)


sathu = Person.age_from_year('Sathvika',1997)
print(sathu.description())

