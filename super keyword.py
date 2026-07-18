class parentclass:
    def parentmethod(self):
        print("this is parent class method")
        
class childclass(parentclass):
    def parentmethod(self):
        print("praksash")
        super().parentmethod()
    
    def childclassmethod(self):
        print("this is child class method");
        super().parentmethod()
        
child=childclass()
child.childclassmethod()
child.parentmethod()            