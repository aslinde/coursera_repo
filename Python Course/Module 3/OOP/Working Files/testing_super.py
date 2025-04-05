class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):
    def speak(self):
        print("Dog barks")
        Animal.speak(self)  # Manual parent call

d = Dog()
d.speak()


class A:
    def __init__(self):
        print("A init")

class B(A):
    def __init__(self):
        A.__init__(self)
        print("B init")

class C(A):
    def __init__(self):
        A.__init__(self)
        print("C init")

class D(B, C):
    def __init__(self):
        B.__init__(self)
        C.__init__(self)
        print("D init")

d = D()

print("----New Code with Super()----")
class A:
    def __init__(self):
        print("A init")

class B(A):
    def __init__(self):
        super().__init__()
        print("B init")

class C(A):
    def __init__(self):
        super().__init__()
        print("C init")

class D(B, C):
    def __init__(self):
        super().__init__()
        print("D init")

d = D()
