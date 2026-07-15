# class person:
#     name="prakash",
#     age="24",
#     profession="IT officer"
    
# a=person()
# print(a.name)
# a.name="suvam"
# print(a.name)

# self keyword

class details:
    name='harry'
    qualification='Engineering'
    networth='10 thousand'
    
    def info(self):
        print(f"{self.name} studied {self.qualification}")
        
a=details()
b=details()
a.name="harry"
a.qualification='entrepreneur'
b.name='peter'
b.qualification='spiderman'
    
a.info()
b.info()
    