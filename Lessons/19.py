from time import sleep
from random import randint, choice
from os import system

def binarySearch(alist, item):
  first = 0
  last = len(alist)-1
  found = False

  while first<=last and not found:
    midpoint = (first + last)//2
    print("First is",first)
    print("Last is",last)
    print("Midpoint is", midpoint)
    print("-------------------")
    if alist[midpoint] == item:
      found = True
    else:
      if item < alist[midpoint]:
        last = midpoint-1
      else:
        first = midpoint+1
  return found

testlist = [10, 11, 12, 13, 14]

print(binarySearch(testlist, 14))
print("----------")
print(binarySearch(testlist, 108))