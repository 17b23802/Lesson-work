from time import sleep
from random import randint, choice

correct = 0
repeats = 0
try:
  times_table = float(input("Welcome to the times table generator. Enter a times table that you would like to display:"))
except ValueError:
  times_table = input("You must enter a number")
try:
  max_value = int(input("Enter the maximum value for your times table:"))
except ValueError:
  print("You must enter a number")
  max_value = int(input())
answer = 0
print(f"Here is the {times_table} times table")
for x in range(1,max_value):
    answer = x * times_table
    print(f"{x} times {times_table} is {answer}")

try:
  times_table = float(input("Welcome to the times table test! What times table would you like to practice?:"))
except ValueError:
  times_table = input("You must enter a number")
try:
  max_value = int(input("Enter the highest multiple you want to use:"))
except ValueError:
  print("You must enter a number")
  max_value = int(input())
answer = 0
for x in range(1,max_value):
  try:
    attempt = float(input(f"What is {x} times {times_table} "))
  except ValueError:
    attempt = float(input("It has to be a number"))
  answer = x * times_table
  if attempt == answer:
    print("Correct!")
    correct = correct + 1
  else:
    print("No,",x,"times",times_table,"is",answer)
  repeats = repeats + 1
print("Done! You got",correct,"right out of",repeats)
