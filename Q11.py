# 11. Write a class that overrides the ___str__` and `___add__`magic methods. What will these methods allow you to do?

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"Vector({self.x}, {self.y})"

    def __add__(self, other):
        if isinstance(other, Vector):
            return Vector(self.x + other.x, self.y + other.y)
        return NotImplemented

if __name__ == "__main__":
    v1 = Vector(2, 3)
    v2 = Vector(4, 5)

    print(v1)              
    print(v2)              

    v3 = v1 + v2          
    print(v3)             
