from time import sleep
from random import randint, choice

def A():
  attempts = 1
  number = 0
  end = 1
  while end == 1:
    added_number = int(input("Input a number"))
    number = number + added_number
    conntinue = input("Do you want to average the current inputs(avg), add another input(add) or quit the program(quit)?").lower()
    if conntinue == "add":
      print("The programme will continue")
      attempts = attempts + 1
    elif conntinue == "avg":
      print("The computer will calculate the averages now")
      end = 2
    else:
      print("The programme will end now. Either you said to end or used an invalid input. The valid inputs are avg or add")
      end = 0
  if end == 2:
    number = number / attempts
    print("The average is",number)