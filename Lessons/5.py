from time import sleep
from random import randint, choice

print("What is your name?")
name = input().lower() 
if name == "anakin":
  print("How do you do Anakin!")
elif name == "Leia":
  print("May the force be with you")
else:
  print(f"Nice name, {name}")
print(f"So {name}, is it hot or cold where you are today?")
weather = input().upper()
if weather == "COLD":
  print("You must be freezing!")
elif weather == "HOT":
  print("Drink plenty of water")
else:
  print("I can't advise you on that type of weather.")
print("Do you like the colour blue?")
likes_blue = input().lower()
if likes_blue == "yes":
  print("I like blue too")
else:
  print("That’s a shame because I really like blue")
dog_breed = input("What is your favourite breed of dog?").lower()
if dog_breed == "poodle":
  print("What is wrong with you?")
elif dog_breed == "labrador":
  print("Cool, I have a labrador")
else:
  print("Cool")
print("Have a good day! Bye!")