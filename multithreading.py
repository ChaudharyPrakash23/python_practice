import threading
import time
from concurrent.futures import ThreadPoolExecutor

def my_function(seconds):
    print(f"sleep for {seconds} seconds")
    time.sleep(seconds)
    
time1=time.perf_counter()
# my_function(4)
# my_function(2)
# my_function(2)
time2=time.perf_counter()
print(time2-time1)

# using threads
t1=threading.Thread(target=my_function,args=[4])
t2=threading.Thread(target=my_function,args=[2])
t3=threading.Thread(target=my_function,args=[1])

time2=time.perf_counter()
print(time2-time1)

t1.start()
t2.start()
t3.start()

#  cuncurrent features
def poolingDemo():
    # 2. Fixed spelling here: ThreadPoolExecutor
    with ThreadPoolExecutor() as executor:
        l = [3, 5, 1, 2]
        results = executor.map(my_function, l)
        for result in results:
            print(result)

poolingDemo()