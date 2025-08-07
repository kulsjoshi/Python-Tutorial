#  Lesson 10: Basic OOP in Python
# 🧠 What You’ll Learn
# How to define a class
# How to create objects
# How to use constructors and methods

#Example One
class Person:
    def __init__(self,name,age):
        self.name = name
        self.age=age
        
    def greet(self):
        print(f"Hello, I'm {self.name} and I'm {self.age} years old")
        
#create an object
p1 = Person("Kuldeep", 100)
p2 = Person("Vaidehi", 2)

#call an object
p1.greet()
p2.greet()

print("+++++++++++++++++++")

#Example 2
class Car:
    def __init__(self,brand,year):
        self.brand=brand
        self.year=year
        
    def display(self):
        print(f"{self.brand} is built in {self.year}")
        
#create an object
teslaCar = Car("Tesla",2024)
toyotaCar = Car("Toyota",1999)

#call an object
teslaCar.display()
toyotaCar.display()