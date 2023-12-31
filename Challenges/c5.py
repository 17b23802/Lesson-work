from time import sleep
from random import randint, choice

def A():
  list_of_names = []
  pos=0
  previous = 0
  names = input("Input a list of names (Separate the names with commas)").split(",")
  decision = input("Do you want to print the names in the original order (O) or in reverse (R)")
  if decision == "O":
    print(names)
  if decision == "R":
    names.reverse()
    print(names)