def greet(fx):
    def mfx():
        print("hello , good evening")
        fx()
        print("thankyou for using this function")
    return mfx
@greet
def hello():
    print("this is hello function using greet decorator")
hello()

import logging
def log_function_call(func):
    def decoreated(*args,**kwargs):
        logging.info(f"calling {func.__name__} with args ={args},kwargs={kwargs}")
        result=func(*args,**kwargs)
        logging.info(f"{func.__name__} returned {result}")
        return result
    return decoreated
@log_function_call
def my_function(a,b):
    return a+b;
my_function(3,5)
