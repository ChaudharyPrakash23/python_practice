class Employeee:
    def __init__(self,name,id):
        self.name=name;
        self.id=id;
        
    def showdetails(self):
        print(f"name name is {self.name} and id is {self.id}")

class Programmer(Employeee):
    def show_language(self):
        print(f"{self.name} with id {self.id} likes python")

e1=Employeee("prakash",2345)
e1.showdetails()
e2=Programmer("hari",4324)
e2.show_language()