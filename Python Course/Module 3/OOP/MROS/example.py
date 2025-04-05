class A:
    def __init__(self):
        self.num=12
class B(A):
    def __init__(self):
        super().__init__()
        self.num=1
class C(B):
    pass
print(C.mro( ))
print(C().num)
#print(B().num)