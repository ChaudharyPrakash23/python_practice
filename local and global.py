# x1=4 
# print(x1)

# def hello():
#     print(f"the local x is {x}")
# print(f"the global x is {x1}")

# y=10
# print(y)

x1=5
print(f"before calling hello(),x1={x1}")

def hello():
    global x1
    print(f"before changing x1={x1}")
    x1=20;
    print(f"after changing x1={x1}")
hello()