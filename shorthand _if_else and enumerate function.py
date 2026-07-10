a=20
b=330
print("a") if a>b else print("b")

# multiple else
a=330
b=330
print(a)if a>b else print("=") if a==b else print(b) 

fruits=['apple','banana','grapes']
for index,fruit in enumerate(fruits):
    print(index,fruit)
    
marks=[12,45,64,63,76,98,12]
for index,mark in enumerate(marks,start=1):
    print(index,mark)