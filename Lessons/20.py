from time import sleep
from random import randint, choice
from os import system

def linear_search(items, search_item):
  # Initialise the variables 
  index = -1
  current = 0
  found = False
  # Repeat while the end of the list has not been reached
  # and the search item has not been found
  while current < len(items) and found == False:
      # Compare the current item to the item you are searching for
      if items[current] == search_item:
          index = current
          found = True
      # Proceed to the next item in the list
      current = current + 1
  return index

