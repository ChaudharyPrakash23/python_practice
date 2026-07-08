# subject="python"
# difficulty_level=True
# print(f"the,{subject} is {difficulty_level} difficult")
# doc string
def square(n):
    ''' takes a number and returns its square '''
    return n*n
square(5)
print(square.__doc__)
import this