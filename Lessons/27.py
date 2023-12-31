from time import sleep
from random import randint
from os import system

num1 = int(input())
num2 = int(input())
system('clear')
if num1 == 1 and num2 == 2:
    print("This is true")
else:
    print("This is false")

if num1 != 1 and num2 != 2:
    print("This is not true")
else:
    print("This is true")

if (num1 == 1 or num2 == 1) and (num1 == 2 or num2 == 2):
  print("True")
else:
  print("nope")