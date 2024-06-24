class Shape:
    def __init__(self,length):
        self.length = length
    def area(self):
        raise NotImplementedError("Subclass must implement abstract method")


class Circle(Shape):
    def area(self):
        result = 3.14*self.length*self.length
        return result

class Square(Shape):
    def area(self):
        result = self.length*self.length
        return result

c1 = Circle(3)
print(c1.area())
s1=Square(4)
print(s1.area())


