class myclass:
    def __init__(self,value):
        self.value=value;
    def show(self):
        print(f'the value is {self.value}')
    
    @property
    def tentimes(self):
        return 10*self.value;
    
    @tentimes.setter
    def tentimes(self,new_value):
        self.value=new_value/10
obj=myclass(10)
obj.tentimes=67
print(obj.tentimes)
obj.show()