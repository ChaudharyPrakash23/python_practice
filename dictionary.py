info={'name':'adarsh','age':23,'iseligible':True}
print(info)
print(info['name'])
print(info.get('age'))

print(info.keys())
print(info.values)
for key in info.keys():
    print(f"the value correspond to key {key} is {info[key]}")
    
print(info.items())

for key,value in info.items():
    print(key,value)