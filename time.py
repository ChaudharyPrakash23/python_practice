import time
def usingwhile():
    i=0
    while(i<300):

      i=i+1;
      print(i)
 
init=time.time()
usingwhile() 
print(time.time()-init)


print(4)
time.sleep(3)
print("this is printed after 3 seconds")