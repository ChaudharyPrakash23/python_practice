f=open("myfile.txt",'w')

# while True:
#     line =f.readlines()
#     if not line:
#         break;
#     print(line)
    
lines=['line 1','line 2','line 3']
for line in lines:
  f.write(line+'\n')
  f.close