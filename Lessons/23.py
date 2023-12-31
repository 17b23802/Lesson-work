from time import sleep
from random import randint, choice
from os import system
items=[]
num_items = len(items)
passes = 1
swapped = True
while passes < num_items and swapped == True:
  swapped = False
  for current in range(num_items - passes):
    if items[current] > items[current+1]:
      Swapped = True
      temp = items[current]
      items[current] = items[current+1]
      items[current+1] = temp
  passes = passes + 1
print(items)

items = ["Maya", "Dan", "Vivian", "Tobi", "Areeji","Steven","Annoying","Zybra"]
num_items = len(items)
for first_unordered in range(1, num_items):
  print("a")
  value = items[first_unordered]
  current = first_unordered - 1
  while current >= 0 and items[current] > value:
    items[current+1] = items[current]
    current = current - 1
  items[current+1] = value
print(items)