"""
1.Multiple Inheritance:
Create a class Flying with a method fly and another class Swimming with a method swim.
Then create a class Duck that inherits from both Flying and Swimming and demonstrate calling both methods on a Duck object.
"""
class Flying:
    def fly(self):
        print("Flying")
class Swimming:
    def swim(self):
       print("Swimming")
class Duck(Flying,Swimming):
    pass
duck = Duck()
duck.fly()
duck.swim()
"""
2. Property Decorators:
Define a class Circle with a private attribute _radius. Use the @property decorator to create a getter and setter 
for the radius attribute. Ensure the setter validates that the radius is a non-negative value.
"""
class Circle:
    def __init__(self,radius):
        self.__radius = radius

    @property
    def get_radius(self):
        return self.__radius
    @get_radius.setter
    def set_radius(self,radius):
        if radius > 0:
            self.__radius = radius

c = Circle(5)
print(c.get_radius)
c.set_radius = 10
print(c.get_radius)
"""
3.Class Method and Static Method:
Extend the Temperature class to include a class method from_kelvin that creates a Temperature instance from a Kelvin value. 
Also, add a static method kelvin_to_celsius that converts Kelvin to Celsius.
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

    @staticmethod
    def kelvin_to_celsius(kelvin):
        return kelvin - 273.15
    @classmethod
    def from_kelvin(cls,kelvin):
        celsius = cls.kelvin_to_celsius(kelvin)
        return cls(celsius)
    @classmethod
    def from_celsius(cls,celsius):
        kelvin = celsius + 273.15
        return cls(kelvin)
    def __int__(self,kelvin):
        self.kelvin = kelvin

temp2 = Temperature.from_celsius(35)


#temp = Temperature(25)
#print(f"25 Celsius in Fahrenheit is {Temperature.celsius_to_fahrenheit(25)}")
#temp1 = Temperature.from_kelvin(300)
#print(temp1.celsius)

print(temp2)

"""
4.Abstract Base Class:
Use the abc module to define an abstract base class Shape with an abstract method area. 
Create subclasses Circle and Square that implement the area method.
"""
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side * self.side

c = Circle(5)
s = Square(4)
print(c.area())  # Output: 78.5
print(s.area())  # Output: 16

"""
5.Operator Overloading:
Define a class ComplexNumber with attributes real and imaginary.
Implement methods to overload the +, -, *, and / operators for complex number arithmetic.
"""
class ComplexNumber:
    def __init__(self,real,imaginary):
        self.real = real
        self.imaginary = imaginary

        def __add__(self, other):
            return ComplexNumber(self.real + other.real, self.imaginary + other.imaginary)

        def __sub__(self, other):
            return ComplexNumber(self.real - other.real, self.imaginary - other.imaginary)

        def __mul__(self, other):
            real = self.real * other.real - self.imaginary * other.imaginary
            imaginary = self.real * other.imaginary + self.imaginary * other.real
            return ComplexNumber(real, imaginary)

        def __truediv__(self, other):
            denominator = other.real ** 2 + other.imaginary ** 2
            real = (self.real * other.real + self.imaginary * other.imaginary) / denominator
            imaginary = (self.imaginary * other.real - self.real * other.imaginary) / denominator
            return ComplexNumber(real, imaginary)

        def __str__(self):
            return f"{self.real} + {self.imaginary}i"

c1 = ComplexNumber(3, 2)
c2 = ComplexNumber(1, 7)
print(c1 + c2)  # Output: 4 + 9i
print(c1 - c2)  # Output: 2 - 5i
print(c1 * c2)  # Output: -11 + 23i
print(c1 / c2)  # Output: 0.34 - 0.38i

"""
6.Iterator Protocol:
Create a class Fibonacci that implements the iterator protocol to generate an infinite sequence of Fibonacci numbers.
"""
class Fibonacci:
    def __iter__(self):
        self.a,self.b = 0,1
        return self
    def __next__(self):
        fib = self.a
        self.a,self.b = self.b,self.a+self.b
        return fib
fib = Fibonacci()
fib_iter = iter(fib)
for _ in range(10):
    print(next(fib_iter),end="")








