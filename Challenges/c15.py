from time import sleep
from random import randint, choice
from os import system
from termcolor import colored

def A():
  not_valid = True
  while not_valid:
    try:
      cost=int(input("Enter the cost of the item in pence"))
      not_valid = False
    except ValueError:
      print("Has to be an interger")
  not_valid = True
  while not_valid:
    try:
      given=int(input("Input how much money you were given in pence"))
      not_valid = False
    except ValueError:
      print("Has to be an interger")

  change=given-cost
  final_change = change
  pound=0
  p50=0
  p20=0
  p10=0
  p5=0
  p2=0
  p1=0
  while change != 0:
    if change - 100 >= 0:
      change = change - 100
      pound=pound+1
    elif change - 50 >= 0:
      change = change - 50
      p50 = p50 + 1
    elif change - 20 >= 0:
      change = change - 20
      p20 = p20 + 1
    elif change - 10 >= 0:
      change = change - 10
      p10 = p10 + 1
    elif change - 5 >= 0:
      change = change - 5
      p5 = p5 + 1
    elif change - 2 >= 0:
      change = change - 2
      p2 = p2+1
    elif change - 1 >= 0:
      change = change - 1
      p1 = p1+1
 

  print(f"Your total change is {final_change} pence")
  if pound > 0:
    print(f"{pound} £1 coins should be given")
  if p50 > 0:
    print(f"{p50} 50p coins should be given")
  if p20 > 0:
    print(f"{p20} 20p coins should be given")
  if p10 > 0:
    print(f"{p10} 10p coins should be given")
  if p5 > 0:
    print(f"{p5} 5p coins should be given")
  if p2 > 0:
    print(f"{p2} 2p coins should be given")
  if p1 > 0:
    print(f"{p1} 1p coins should be given")