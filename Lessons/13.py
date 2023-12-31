from time import sleep
from random import randint, choice
from os import system

stored_pass = "password"
password = ""
pass_mismatch = stored_pass != password

while pass_mismatch:
  password = input("Enter your password: ")
  pass_mismatch = stored_pass != password
print("Access granted")
sleep(1)
system('clear')

fizz = input("Welcome to fizzbuzzbang! Enter a name for fizz")
notvalidated = True
while notvalidated:
  try:
    fizzvalue = int(input("Enter a number for fizz"))
    notvalidated=False
  except ValueError:
    print("It has to be an interger")
buzz = input("Enter a name for buzz")
notvalidated = True
while notvalidated:
  try:
    buzzvalue = int(input("Enter a value for buzz"))
    notvalidated=False
  except ValueError:
    print("It has to be an interger")
bang = input("Enter a value for bang")
notvalidated = True
while notvalidated:
  try:
    bangvalue = int(input("Enter a value for bang"))
    notvalidated=False
  except ValueError:
    print("It has to be an interger")
maximum = 1 + int(input("Enter the value the pattern will go to"))
print("Now start the pattern")
i = 1
while i < maximum:
  if i % fizzvalue == 0 and i % buzzvalue == 0 and i % bangvalue == 0:
    correct = fizz+buzz+bang
  elif i % fizzvalue == 0 and i % buzzvalue == 0:
    correct = fizz+buzz
  elif i % buzzvalue == 0 and i % bangvalue == 0:
    correct = buzz+bang
  elif i % fizzvalue == 0 and i % bangvalue == 0:
    correct = fizz+bang
  elif i % fizzvalue == 0:
    correct = fizz
  elif i % 5 == 0:
    correct = buzz
  elif i % 4 == 0:
    correct = bang
  else:
    correct = str(i)
  inpot = input(Fore.YELLOW+"Enter the next part: ")
  if inpot == correct:
    print(Fore.GREEN+"Correct!")
  else:
    print(Fore.RED+"WRONG! You lose!")
    i = maximum + 1
  i = i + 1