#define a class "car"
class Car:

    #attributes
    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year

#object
car1 = Car("Honda","Accord",2008)

print(f"My car is a {car1.make} {car1.model} {car1.year}")
