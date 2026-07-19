class Employee:
    def __init(self,name):
        self.name=name;
        
class Dancer:
    def __init__(self,dance):
        self.dance=dance
    
class DancerEmployee(Employee,Dancer):
    def __init__(self,name,dance):
        self.dance=dance;
        self.name=name;
        
DE=DancerEmployee("shivani","hiphop")
print(DE.name)
print(DE.dance)
print(DancerEmployee.mro())