# 6. Describe the five types of inheritance in Python. Provide a simple example of multiple inheritance.

# Single Inheritance
class Animal:
    def speak(self):
        return "Animal speaks"

class Dog(Animal):
    def bark(self):
        return "Woof!"

dog = Dog()
print(dog.speak())  
print(dog.bark())   

# Multiple Inheritance
class Parent1:
    def method1(self):
        return "Method from Parent1"

class Parent2:
    def method2(self):
        return "Method from Parent2"

class Child(Parent1, Parent2):
    def child_method(self):
        return "Method from Child"

child = Child()
print(child.method1())  
print(child.method2())  
print(child.child_method())  

# Multilevel Inheritance
class Grandparent:
    def method_grandparent(self):
        return "Method from Grandparent"

class Parent(Grandparent):
    def method_parent(self):
        return "Method from Parent"

class Child(Parent):
    def method_child(self):
        return "Method from Child"

child = Child()
print(child.method_grandparent())  
print(child.method_parent())        
print(child.method_child())         
 	
# Hierarchical Inheritance
class Vehicle:
    def type(self):
        return "Vehicle type"

class Car(Vehicle):
    def wheels(self):
        return 4

class Bike(Vehicle):
    def wheels(self):
        return 2

car = Car()
bike = Bike()
print(car.type())  
print(car.wheels())  
print(bike.type())  
print(bike.wheels())  

# Hybrid Inheritance
class A:
    def method_a(self):
        return "Method from A"

class B(A):
    def method_b(self):
        return "Method from B"

class C(A):
    def method_c(self):
        return "Method from C"

class D(B, C):
    def method_d(self):
        return "Method from D"

d = D()
print(d.method_a())  
print(d.method_b())  
print(d.method_c())  
print(d.method_d())  
