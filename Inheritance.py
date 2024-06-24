class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def greet(self):
        return f"Hello I'm {self.name} and I'm {self.age} years old!"

class Student(Person):
    def __init__(self,name,age,student_id):
        super().__init__(name,age)
        self.student_id = student_id



person1 = Student('sathu',18,"12345")
print(person1.greet())
