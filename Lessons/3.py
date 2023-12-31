from time import sleep
from random import randint, choice


name = input("Hello! I am the mystical magician, magic Merry! What is your name?")
number = int(input(f"Hello {name}, I can amaze you with a simple numbers trick! Pick a number."))
print("Now times you number by 10...")
sleep(3)
print("Divide the new number by the original number...")
sleep(3)
print("And your new number is... give a minute...")
sleep(60)
number = number * 10 / number
print(number,"!")


print("Hello my name is Susan from space")
name = input("What is your name?")
print(f"Hello {name}. I am from the year 2210 and I am 20 years old")
age = int(input("How old are you? "))
future_age=age+2210-2020
print(f"Wow, by 2210 you will be {future_age}, that is really old!")
music = input("What type of music are you into?")
print(f"I have not heard of {music}")
society = input("Has your society crumbled yet?")
if society == "yes"or"Yes"or"YES":
  live = input("Do you want to live with me?")
  if live.lower == "yes":
    print("Yay! Prepare to be abducted!")
  else:
    print("Well flip you too")
else:
  print("Well ok then.")