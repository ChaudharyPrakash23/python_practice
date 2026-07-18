class Employee:
    companyName="Apple"
    def show(self):
        print(f"the name is {self.name} and company is {self.companyName}")
    
    @classmethod
    def changeCompany(cls,newCompany):
        cls.companyName=newCompany

e1=Employee()
e1.name="harry"
e1.show()
e1.changeCompany("tesla")
e1.show()
print(Employee.companyName)