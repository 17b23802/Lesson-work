from time import sleep
from random import randint, choice
from termcolor import colored


print(colored("Pick either ostrich, lion, fish, whale, carrot, sweetcorn, brocoli or peas",'magenta'))
print(colored("I will attempt to guess your choice",'yellow'))
answer = input("Is it an animal? Y/N").lower
if answer == "y":
  print("Does the animal live in the water? Y/N")
  answer = input().lower()
  if answer == "n":
    print("Does the animal have wings? Y/N")
    answer = input().lower()
    if answer == "y":
        print("It must be an Ostrich!")
    else:
        print("It must be a Lion!")
  else:
    print("Is it a mammal? Y/N")
    answer = input().lower()
    if answer == "n":
      print("It must be a Fish!")
    else:
      print("It must be a Whale!")

elif answer == "n":
  answer = input("Is your vegetable green? Y/N").lower
  if answer == "y":
    answer = input("Does it look like a tree? Y/N").lower
    if answer == "y":
      print(colored("Then it's brocoli!",'green'))
    elif answer == "n":
      print(colored("Then it's peas!",'green'))
    else:
      print(Fore.RED + "Not a valid input")
  elif answer == "n":
    answer = input("Is it orange? Y/N").lower
    if answer == "y":
      print(Fore.ORANGE + "Then it's carrot!")
    elif answer == "n":
      print(Fore.YELLOW + "Then it's sweetcorn!")
    else:
      print("Not a valid input")
  else:
    print(Fore.RED + "Not a valid input")
else:
  print(Fore.RED + "Not a valid input")