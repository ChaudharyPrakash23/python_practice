# a=input("Enter a number :")
# print(f"the multiplication of {a} is :")
# try:
#  for i in range (1,11):
#    print(f"{int(a)} x {i}= {int(a)*i}")     
# except:
#      print("Enter the valid number")

a=23
b=0;
try:
 result=a/b
except ArithmeticError:
    print("cannot divie by 0")