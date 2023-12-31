from time import sleep
from random import randint, choice
from os import system

def A():
  def invalid_input():
    print("This is not a valid input. Please retry.")
  shopping = []
  editing_list = True
  while editing_list:
    print("Would you like to edit your shopping list? Y/N")
    edit = input().upper()
    if edit == "N":
      editing_list = False
    elif edit == "Y":
      print("Would you like to add or remove an item? A/R")
      edit_type = input().upper()
      if edit_type == "A":
        item = input("Enter an item to add:").lower()
        shopping.append(item)
      elif edit_type == "R":
        item = input("Enter an item to remove:").lower()
        shopping.remove(item)
      else:
        invalid_input()
    else:
      invalid_input()
  print("Your shopping list is",shopping)