from time import sleep
from random import randint, choice

def A():
  print("Welcome to my pizza!")
  sleep(3)
  option = input("Do you want to divide the slices or calculate the bill?(1 or 2)")
  if option == 1:
    try:
      slices = int(input("How many slices are there?"))
    except ValueError:
      print("It has to be an interger")
      slices = int(input("How many slices are there?"))
    try:
      people = int(input("How many people are there?"))
    except ValueError:
      print("It has to be an interger")
      people = int(input("How many people are there?"))
    slices_per_person = slices // people
    remainder = slices % people
    print("Each person will have ",slices_per_person,"slices with",remainder,"left over!")
    option = input("Do you want to also calculate the bill?")

  if option == 2 or option == "yes" or option == "Yes" or option == "YES":
    try:
      bill_total = float(input("What is the total bill?"))
    except ValueError:
      print("It has to be a number")
      bill_total = float(input("What is the total bill?"))
    try:
      tip_percentage = int(input("What percentage tip would you like to leave?"))
    except ValueError:
      print("It has to be an interger")
      tip_percentage = int(input("What percentage tip would you like to leave?"))
    cost_per_person = (bill_total + bill_total * tip_percentage / 100) / people
    print(f"Total bill including tip is £{bill_total}")
    print(f"Total cost per person is £{cost_per_person}")