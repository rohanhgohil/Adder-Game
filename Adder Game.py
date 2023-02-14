import random
import sys
chance=3
level=1
randomrange=0

while True:
  if level<1:
    print("You should start Maths from nursery.")
    print("Bbye! Take care. See yaa")
    break
  rand1=random.randint(10**(level-1),10**(level)-1)
  rand2=random.randint(10**(level-1),10**(level)-1)
  
  print(" ",rand1,"\n+",rand2)
  user=int(input("Enter the answer:"))
  if user==0:
    break
  elif rand1+rand2==user:
    print("Correct Answer!\nLevel UP")
    level=level+1
    chance=3
  elif rand1+rand2!=user:
    print("Wrong Answer!")
    chance=chance-1
    if chance==0:
      print("Oops!Level Down")
      level=level-1
      chance=3
    else:
      pass
  else:
    pass
      
