# str and repr
class student:
    def __init__(self,name):
        self.name=name;
    def __str__(self):
        return f"student name is {self.name}"
    
    def __repr__(self):
        return f"{self.name}"

s=student("prakash")
print(s)
print(repr(s))

# len

class Books:
    def __init__(self):
        self.books_list=["maths","python","Engineering drawing"]
        
    def __len__(self):
        return len(self.books_list)
    
B=Books()
print(len(B))

# call

class student:
    def __call__(self):
        print("Object is called like an function")

s=student()
s()