def cube(x):
    return x*x*x;

numbers=[1,2,3,4,5,6]
cubenumbers=list(map(cube,numbers))
print(cubenumbers)

double=list(map(lambda x:x*2,numbers))
print(double)

# filter

filtered=list(filter(lambda x:x>4,numbers))
print(filtered)

# reduce
from functools import reduce
sum=reduce(lambda x,y:x+y,numbers)
print(sum)