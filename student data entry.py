import pickle as pick
i=input('enter file address')
def read():
  f=open('i','r')
  try:
    while True:
      r=pick.load(f)
      print(r,'/n')
   except:
     f.close()
      
def write():
  f=open('i','a')
  data={}
  stud=[]
  i=int(input('enter number of records'))
  for j in range(i):
      data['name']=input('name:')
      data['roll']=int(input('roll number:'))
      data['marks]=int(input('marks'))
      stud.append(data)
      pick.dump(f,stud)
      
