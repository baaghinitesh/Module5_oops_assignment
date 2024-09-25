# 5. What are the three types of access modifiers in Python? How are they denoted?

# Public- Example:
class MyClass:
    def __init__(self):
        self.public_attribute = "I am public"

obj = MyClass()
print(obj.public_attribute)  

# Protected - Example:
class MyClass:
    def __init__(self):
        self._protected_attribute = "I am protected"

class SubClass(MyClass):
    def access_protected(self):
        return self._protected_attribute

obj = SubClass()
print(obj.access_protected())  

# Private - Example:
class MyClass:
    def __init__(self):
        self.__private_attribute = "I am private"

    def get_private(self):
        return self.__private_attribute

obj = MyClass()
print(obj.get_private()) 
