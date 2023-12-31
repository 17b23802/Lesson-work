from time import sleep
from random import randint, choice
from os import system

def add(a, b,c):
  answer = a + b + c
  print(f"{a} + {b} + {c} = {answer}")

def average_value(a,b,c):
  average = (a+b+c)/3
  print("The average value is", average)

def highest(a,b,c):
  if a > b and a>c:
    print("The highest number is",a)
  elif b>a and b>c:
    print("The highest number is",b)
  elif c>a and c>b:
    print("The highest number is",c)
  else:
    print("They are the same number")

def lowest(a,b,c):
  if a < b and a<c:
    print("The lowest number is",a)
  elif b<a and b<c:
    print("The lowest number is",b)
  elif c<a and c<b:
    print("The lowest number is",c)

def multiply(a,b,c):
  answer = a*b*c 
  print(a,"x",b,"x",c,"=",answer)

def subtract(a,b,c):
  print(a,"-",b,"-",c,"=",a-b-c)

def divide(a,b,c):
  print(a,"/",b,"/",c,"=",a/b/c)

print("Enter a number:")
not_done = True
while not_done:
  try:
    num1 = int(input())
    not_done = False
  except ValueError:
    print("Has to be an interger")
system('clear')
not_done = True
while not_done:
  try:
    print("Enter another number:")
    num2 = int(input())
    not_done = False
  except ValueError:
    print("Has to be an interger")
system('clear')
print("Enter another number")
not_done = True
while not_done:
  try:
    num3 = int(input())
    not_done = False
  except ValueError:
    print("Has to be a number")
system('clear')

not_finished = True
while not_finished:
  decision = input("Do you want to +, -, *, /, average, find the highest number, or find the lowest number? Put done if you don't want to.").lower()
  if decision == "+":
    add(num1, num2, num3)
  elif decision == "average":
    average_value(num1,num2,num3)
  elif decision == "highest":
    highest(num1,num2,num3)
  elif decision == "lowest":
    lowest(num1,num2,num3)
  elif decision == "*":
    multiply(num1,num2,num3)
  elif decision == "-":
    subtract(num1,num2,num3)
  elif decision == "/":
    divide(num1,num2,num3)
  elif decision == "+ - * / average highest or lowest":
    print("Idiot")
  elif decision == "done":
    print("Goodbye")
    not_finished = False
  else:
    print("Not a valid input. It only accepts + - * / average highest or lowest")