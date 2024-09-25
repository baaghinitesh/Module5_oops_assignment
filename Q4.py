# 4. How does Python implement method overloading? Give an example.

# Example of Method Overloading Using Default Arguments
class Example:
    def greet(self, name=None):
        if name is None:
            print("Hello, World!")
        else:
            print(f"Hello, {name}!")

# Creating an instance of the class
example = Example()

# Calling the method with no arguments
example.greet()  

# Calling the method with one argument
example.greet("Alice")  
 

# Example of Method Overloading by Argument Type Checking
#Example using *args:
class Calculator:
    def add(self, *args):
        return sum(args)

# Creating an instance of the class
calc = Calculator()

# Calling the method with different numbers of arguments
print(calc.add(2, 3))          
print(calc.add(1, 2, 3, 4))    

#Example using **kwargs:
def my_function(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

my_function(name="Alice", age=30) 
