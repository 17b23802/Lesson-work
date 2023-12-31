from random import randint
from os import system

correct=0
intros=0
not_done=True
shopping=[]
simon_says=[]
while not_done:
  instruction=input("Type in an instruction for simon to say. (type end or leave blank to stop inputting instructions)").lower().strip()
  if instruction=="end" or instruction=="":
    if simon_says==[]:
      print("You have to input at least 1 value")
    else:
      not_done=False
  else:
    simon_says.append(instruction)
    
while correct!=-1:
  intro = intros[randint(0,len(intros)-1)]
  try:
    instruction = simon_says[randint(0,len(intros)-1)]
  except IndexError:
    instruction=simon_says[0]
  y=input(f"{intro}{instruction} ")
  if (y=="" and intro=="") or (y==instruction and intro!=""):
    print("That's how you do it!")
    correct=correct+1
  else:
    if y==instruction and intro=="":
      print("I didn't say simon says...")
    else:
      print("Wrong!")
    print(f"You got a total of {correct} instructions correct.")
    correct=-1
  
while correct==-1:
  print(f"Your current shopping list is {shopping}")
  option=input("Should an item be added (a) or removed (r). If you've finished, type end").lower()
  if option == "a":
    item=input("Enter an item to add")
    shopping.append(item)
  elif option =="r":
    item=input("Enter an item to remove")
    shopping.remove(item)
  elif option=="end":
    print(f"Your shopping list is now {shopping}")
    correct==6
  system('clear')