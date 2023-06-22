import pickle as pick
i=input('enter file address')
def read():
  f=open(i,'rb')
  try:
     while True:
        r=pick.load(f)
      print(r)  
     except:
        f.close()
      
def write():
  f=open(i,'wb+')
  data={}
  stud=[]
  i=int(input('enter number of records'))
  for j in range(i):
      data['name']=input('name:')
      data['roll']=int(input('roll number:'))
      data['marks]=int(input('marks:'))
      stud.append(data)
      data={}    
      pick.dump(stud,f)
  f.close()     

