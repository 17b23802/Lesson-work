from time import sleep
from random import randint, choice
from os import system

def even(a):
  if a %2 == 0:
    print("And it's even")
  else:
    print("And it's odd")

def same(a,b):
  if a == b:
    print("They are the same picture")
    even(a)
  else:
    print("They are not the same picture")

Fie1=randint(1,6)
Fie2=randint(1,6)
same(Fie1,Fie2)
print(Fie1)
print(Fie2)
