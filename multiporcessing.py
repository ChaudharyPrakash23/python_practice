import multiprocessing
import requests

def downloadFile(url,name):
    print(f"started downloading {name}")
    response=requests.get(url)
    open(f"files/file{name}.jpg","wb").write(response.content)
    print(f"finished downloading {name}")

url="https://picsum.photos/200/300"

if __name__=='__main__':
 pros=[]

 for i in range(5):
    # downloadFile(url,i)
    p=multiprocessing.Process(target=downloadFile,args=[url,i])
    p.start()
    pros.append(p)
    
 for p in pros:
    p.join()