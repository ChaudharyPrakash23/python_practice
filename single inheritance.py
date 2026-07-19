class Animal:
    def __init__(self,name,species):
        self.name=name;
        self.species=species;
    
    def make_sound(self):
        print("this is sound make by animal")
        
class Dog(Animal):
    def __init__(self,name,breed):
        Animal. __init__(self,name,species="Dog")
        self.breed=breed
    
    def make_sound(self):
        print("bark")
        
d=Dog("dog","doggerman")
d.make_sound()

a=Animal("dog","dog")
a.make_sound()