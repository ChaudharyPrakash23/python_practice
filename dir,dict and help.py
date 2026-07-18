x=[1,2,3,4]
print(dir(x))
print(x.__class__)

class person:
    def __init__(self,name,age):
        self.name=name;
        self.age=age;

p=person("prakash","24")
print(p.__dict__)

class employee:
    def __init__(self,salary):
        self.salary=salary;
e=employee(30000)
print(help(employee))