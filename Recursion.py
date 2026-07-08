def factorial(num):
    if(num==0 or num==1):
        return 1;
    else:
        return(num*factorial(num-1))
print(factorial(6))

# fibonacci series

def fibo(n):
    if(n==0):
        return 0;
    elif(n==1 or n==2):
        return 1;
    else:
        return (fibo(n-1)+fibo(n-2));
print(fibo(6))