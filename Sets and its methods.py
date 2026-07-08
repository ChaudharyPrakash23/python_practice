set1={'carla',12,23,False,5.9,12}
print(set1)
# creating empty set

empty=set()
print(type(empty));

# accessing set elements
info={"carlo",19,False,5.9,19}
for value in info:
    print(value)

# set methods

cities={'kathmandu','pokhara','nepalgunj,butwal'}
cities2={'delhi','kolkotta','banaras','butwal'}
cities3=cities.union(cities2)
print(cities3)
cities.update(cities2)
print(cities,cities2)

# intersection
set1={1,2,4,5,3,6}
set2={1,5,3,10}
print(set1.intersection(set2))
set1.intersection_update(set2)
print(set1)

# symmetric difference and symmetric difference update
setone={"apple","ball","car"}
setwo={"apple","ball","orange"}
setthree=setone.symmetric_difference(setwo)
print(setthree)
setone.symmetric_difference_update(setwo)
print(setone)

print(set1.difference(set2))
setwo.add("banana");
print(setwo)
print(setone.isdisjoint(setwo))
print(setone.issuperset(setwo))
print(setone.issubset(setwo))
set1.update(setwo)
print(setone)
setone.remove("orange")
print(setone)
print(setone.pop())
set2.clear()