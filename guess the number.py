import random as r
n=int(input('enter number up to u want'))
ran=r.randrange(0,n+1)
for j in range(5):
    i=int(input('enter your number'))
    if ran==i:
      print('yes u won')
      break
    elif i > ran:
     print('the number is less than your guess')
    elif i==ran-1:
      print('you are near')
    elif i < ran:
      print('the number is greater than yuor guess')

  
