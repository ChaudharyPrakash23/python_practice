with open('file.txt','r') as f:
    f.seek(10)
    data=f.read(5)
    current_position=f.tell()
    f.seek(current_position)
    print(current_position)
    print(data)
    
    with open ('sample.txt','w') as S:
      S.write("this is sample data")
      S.truncate(5)
      
      with open ('sample.txt','r') as S:
          print(S.read())