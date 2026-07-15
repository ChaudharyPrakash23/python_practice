class person:
    def __init__(self,name,occupation):
        self.name=name
        self.occupation=occupation
        
    def info(self):
        print(f"{self.name} is involved in {self.occupation}")


a=person("prakash","IT engineer")
b=person("sameer",'Hardware engineer')
a.info()
b.info()

class details:
    def __init__(self,animal,group):
        self.animal=animal
        self.group=group
obj1=details("crab","crustanceans")
print(obj1.animal,obj1.group)