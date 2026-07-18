class Myclass:
    class_variable=0;
    def __init__(self):
        Myclass.class_variable +=1;
    def print_class_variable(self):
        print(Myclass.class_variable)
        
obj1=Myclass()
obj2=Myclass()
obj1.print_class_variable()

# instance varaible
class Employee:
   company_name="apple"
   no_of_employee=0
   def __init__(self,name):
       self.name=name;
       self.raise_amount=0.02
       Employee.no_of_employee +=1
   def show_details(self):
       print(f"{self.name},{self.no_of_employee},{self.company_name},{self.raise_amount}")

emp1=Employee("prakash")
emp1.raise_amount=0.03;
emp1.company_name="apple India"
emp1.show_details()     