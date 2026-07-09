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

# try:  
#  l=[1,5,6,7]
#  i=int(input("Enter the index :"))
#  print(l[i])
# except:
#     print("some error occured")
# finally:
#     print("finally iam executed")

salary=500
if not 1000<salary<2000:
    raise ValueError ("not a valid salary")