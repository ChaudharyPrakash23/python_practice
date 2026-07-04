# tup=(1,2,3,4)
# print(type(tup),tup)
# if 3 in tup:
#     print("3 is present")
# else:
#     print(" absent")
animals=('cat','dog','pig','man','bat','cow')
# print(animals[0:5:2])
# tupe operations
listanimal=list(animals)
listanimal.append("buffalo")
animals=tuple(listanimal)
print(animals)

tup=(1,2,3,4,5,1,1,34)
print(tup.count(1))
print(tup.index(2))