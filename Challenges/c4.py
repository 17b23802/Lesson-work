from time import sleep
from random import randint, choice

def A():
  print("PASSWORD TIME BOIS! YOUR PERSONAL INFORMATION GOT LEAKED? WE CAN HELP!")
  password = input("Input a password!")
  passwordtwo = input("Type it in again")
  if password == passwordtwo:
    if password.lower() == password:
      print("Add uppercase characters")
    elif password.upper() == password:
      print("Add lowercase characters")
    elif len(password) < 8:
      print("Too short")
    else:
      print("That's a valid password")