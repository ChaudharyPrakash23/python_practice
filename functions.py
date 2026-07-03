# def geometricmean(a,b):
#     mean=(a+b)/(a-b)
#     print(mean)
    
# geometricmean(4,5)
# def gmean(a,b):
#     if(a>b):
#         print(" first number is greater")
#         mean=(a+b)/(a-b)
#         print(mean)
#     else:
#         print("B is greater")
#         mean=(b+a)/(b-a)
#         print(mean)
# gmean(6,10)        

# def greet(fname,lname="watson"):
#     print("hello",fname,lname)
# greet("anny")

def average(*numbers):
    total=0
    for i in numbers:
        total=total+i;
    avg=total/len(numbers)
    print(avg)
average(2,3,4,5,6);
     