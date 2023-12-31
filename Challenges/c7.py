from time import sleep
from random import randint, choice
from os import system
from termcolor import colored

def A():
  list_length = 0
  counting = 0
  thelist = []
  list2electricboogaloo = []
  letter = input(colored("Select a letter to use ",'yellow'))
  notdone = True
  while notdone:
    addtolist = input(colored("Type a word to add to the list or type * if you've finished adding things to the list",'blue'))
    system('clear')
    if addtolist == "*":
      if list_length > -1:
        notdone = False
      else:
        print("You need to add something to the list")
    else:
      thelist.append(addtolist)
      print(colored("The list so far is",thelist,'green'))
      list_length = list_length+1  
  while counting < list_length:
    if thelist[counting].find(letter) > -1:
      list2electricboogaloo.append(thelist[counting])
    counting= counting + 1
  print(list2electricboogaloo)