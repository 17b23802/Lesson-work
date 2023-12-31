from time import sleep
from random import randint, choice

def A(challenge):
  number = float(input("Add a number to your list "))
  min_num = number
  max_num = number
  while challenge == "c6":
    number = float(input("Add a number to your list "))
    if number > max_num:
      max_num=number
    elif number < min_num:
      min_num = number
    print("The minimum number in your list is",min_num,"and the maximum number in your list is",max_num)