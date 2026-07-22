from functools import lru_cache
import time

@lru_cache(maxsize=None)
def function(n):
    time.sleep(5)
    return n*5;

print(function(20))
print("done for 20");
print(function(4))
print("done for 4");
print(function(6))
print("done for 6");
print(function(20))
print("done for 20");