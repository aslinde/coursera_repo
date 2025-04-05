class myParent:
    def __init__(self):
        self.a = 12

class myChild(myParent):
    pass

object_child = myChild()
print(object_child.a)

class Employees:
    def __init__(self, name, last):
        self.name = name
        self.last = last

class Supervisors(Employees):
    def __init__(self, name, last, password):
        super().__init__(name, last)
        self.password = password
class Chefs(Employees):
    def leave_reqiest(self,days):
        return "May I take a leave for " + str(days) + " days?"
    

adrian = Supervisors("Adrian", "Smith","abc")
emily = Chefs("Emily", "Smith")
juno = Chefs("Juno", "Smith") 

print(emily.leave_reqiest(3))
print(adrian.password)
print(emily.name)