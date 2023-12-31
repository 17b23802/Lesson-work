from time import sleep
from random import randint
from os import system
from termcolor import colored

not_done=True
while not_done:
  try:
    Year = int(input("Enter the year you joined the school: "))
    not_done = False
  except ValueError:
    print(colored("Has to be a number",'red'))
    sleep(1)
    system('clear')
Year=str(Year)
FirstName=input("Enter your first name: ")
Surname = input("Enter your surname: ")
username=Year[len(Year)-2]+Year[len(Year)-1]+Surname+FirstName[0]
print("Your username is",username)

sleep(3)
system('clear')

username=input("Enter your username: ")
print("You are in year",27-int(username[0]+username[1]))

sleep(3)
system('clear')

not_done=True
while not_done:
  Inputted_password=input("Input password: ")
  if len(Inputted_password)>7:
    if "0" in Inputted_password or "1" in Inputted_password or "2" in Inputted_password or "3" in Inputted_password or "4" in Inputted_password or "5" in Inputted_password or "6" in Inputted_password or "7" in Inputted_password or "8" in Inputted_password or "9":
      print("Valid password")
      not_done=False
    else:
      print("No number")
  else:
    print("Not long enough")

sleep(3)
system('clear')

message=""
notDone=True
while notDone:
  not_done=True
  while not_done:
    try:
      Code=input(f"Enter the deciaml number or type Done if you've finished. The code so far is {message}: ").lower()
      if Code == "done":
        notDone=False
      else:
        Code=int(Code)
        Code = chr(Code)
        message = message + Code
      not_done = False
    except ValueError:
      print(colored("Has to be a number",'red'))
print("The message is",message)

message=""
Code=input("Enter the message you want to encode: ")
for x in Code:
  Temp=ord(Code[x])
  message=message+Temp
print("The message is",message)