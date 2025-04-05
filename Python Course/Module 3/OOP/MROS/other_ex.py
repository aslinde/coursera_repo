# Example 1
class A:
   def a(self):
       return "Function inside A"

class B:
    def a(self):
        return "Function inside B"

class C(B,A): ### To me it looks like when it finds the first a method inside a class it's done
              ### It doesn't taka the last value which would be logical if it goes from left to right
    pass       

# Driver code
c = C()
print(c.a())

#Example 2
print("---- New Example ----")
class A:
    def b(self):
        return "Function inside A"

class B:
    def b(self):
        return "Function inside B"

class C(A, B):
    def b(self):
        return "Function inside C" ## If you comment these out it returns class A b function 
    pass                           ## Because it is the first method found

class D(C):
    pass

d = D()
print(d.b())

#Example 3
print("---- New Example ----")
class A:
    def c(self):
        return "Function inside A"

class B:
    def c(self):
        return "Function inside B"

class C(A, B):
    def c(self):
        return "Function inside C"

#class D(A, C):
  #  pass

#d = D()
#print(d.c())

# Example 4
print("---- New Example ----")
class A:
    def d(self):
        return "Function inside A"

class B:
    def d(self):
        return "Function inside B"


class C:
    def d(self):
        return "Function inside C"


class D(A, B):
    def d(self):
        return "Function inside D"


class E(B, C):
    def d(self):
        return "Function inside E"


class F(E,D,C):
    pass

f = F()
print(f.d())
print(F.mro())