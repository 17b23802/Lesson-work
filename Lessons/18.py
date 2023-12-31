from time import sleep
from random import randint, choice
from os import system

notDone=True
thelist = []
while notDone:
  add = input("Add a word to the list or type * if you're done:").lower()
  system('clear')
  if add=="*":
    notDone=False
  else:
    thelist.append(add)
searchFor=input("Which word are you looking for?").lower()

notDone = True
attempts = 0
for tries in thelist:
  if notDone:
    attempts = attempts+1
    if tries == searchFor:
      notDone = False

if notDone:
  print("It is not in the list")
else:
  print("It is in position",attempts,"in the list")