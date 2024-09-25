# 9. Demonstrate polymorphism by creating a function that can work with different shape objects to calculate and print their areas.

from abc import ABC, abstractmethod
import math

# Abstract base class
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

# Subclass for Circle
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)

# Subclass for Rectangle
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

# Function to calculate and print area of a shape
def print_area(shape: Shape):
    print(f"The area is: {shape.area():.2f}")


if __name__ == "__main__":
    circle = Circle(5)
    rectangle = Rectangle(4, 6)

    print_area(circle)    
    print_area(rectangle)  
