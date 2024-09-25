# 7. What is the Method Resolution Order (MRO) in Python? How can you retrieve it programmatically?

class A:
    pass

class B(A):
    pass

class C(A):
    pass

class D(B, C):
    pass

# Retrieve MRO
print(D.__mro__)

print(D.mro())
