# public modifiers

class student:
    def __init__(self,name,age):
        self.name=name;
        self.age=age;
obj1=student("rahul",21)
print(obj1.name,obj1.age)

# private
class employee:
    def __init__(self,name,salary):
        self.__name=name;
        self.salary=salary
obj=employee("prakash",30000)
# print(obj.___name) cannot be accessed
print(obj._employee__name)  
# accessed using name mangling


# protected

class Teacher:
    def __init__(self):
        self._name="prakash"
    
    def _funName(self):
        return "my name is prakash";

class staff(Teacher):
    pass

object1=Teacher()
object2=staff()
print(object1._name)
print(object1._funName())

print(object2._name)
print(object2._funName())