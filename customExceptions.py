class customError(Exception):
    pass
num=input("Enter a number")
if num=="not an error":
    print("error cannot be raised in this")
else:
    try:
         int(num)
         print("it is an integer")  
    except ValueError:
        raise customError ("please enter an integer")
        