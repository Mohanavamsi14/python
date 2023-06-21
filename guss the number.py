import random as r
ran=r.randrange(0,101)
i=int(input('enter your number'))
if ran==i:
  print('yes u won')
elif i > ran:
 print('you are going to fast')
elif i==ran-1:
  print('you are near')
elif i<ran:
  print('the number is after your number')

  
