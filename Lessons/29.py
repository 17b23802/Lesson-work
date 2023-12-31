from time import sleep
from os import system
uses = 0
not_ended = True
adultPrice = 20
childPrice = 12
seniorPrice = 11
wristbandPrice = 20

def Admin():
  print("Admin mode activated")
  notDone = True
  while notDone:
    try:
      tempAdult = int(input("What is the new adult ticket price?"))
      notDone = False
    except ValueError:
      print("It has to be a number")
  notDone = True
  while notDone:
    try:
      tempChild = int(input("What is the new child ticket price?"))
      notDone = False
    except ValueError:
      print("It has to be a number")
  notDone = True
  while notDone:
    try:
      tempSenior = int(input("What is the new senior ticket price?"))
      notDone = False
    except ValueError:
      print("It has to be a number")
  notDone = True
  while notDone:
    try:
      tempWristband = int(input("What is the new wristband price?"))
      notDone = False
    except ValueError:
      print("It has to be a number")
  return [tempAdult, tempChild, tempSenior, tempWristband]

def TicketAdult():
  not_done = True
  while not_done:
    try:
      adultTicket = int(input("How many adult tickets do you want? "))
      not_done = False
    except ValueError:
      print("Has to be a number")
  return adultTicket

def TicketChild():
  not_done = True
  while not_done:
    try:
      childTicket = int(input("How many child tickets do you want? "))
      not_done = False
    except ValueError:
      print("Has to be a number")
  return childTicket

def TicketSenior():
  not_done = True
  while not_done:
    try:
      seniorTicket = int(input("How many senior tickets do you want? "))
      not_done = False
    except ValueError:
      print("Has to be a number")
  return seniorTicket

def AmmountWristband():
  not_done = True
  while not_done:
    try:
      wristbandAmmount = int(input("How many wristbands do you want? "))
      not_done = False
    except ValueError:
      print("Has to be a number")
  return wristbandAmmount

def SurnameInput():
  return input("What is the surname of the person purchasing the tickets? ")

def ParkPass():
  not_done = True
  while not_done:
    parkPass = input("Do you require a parking pass? y/n ").lower()
    if parkPass == "y" or parkPass == "n":
      not_done = False
  return parkPass

def CostCalculator(adultTicket,adultPrice,childTicket,childPrice,seniorTicket,seniorPrice,wristbandAmmount,wristbandPrice):
  return adultTicket*adultPrice+childTicket*childPrice+seniorTicket*seniorPrice+wristbandAmmount*wristbandPrice

def Payment(tempTotal):
  not_done = True
  while not_done:
    if tempTotal >= 0:
      not_done = False
    else:
      notDone = True
      while notDone:
        try:
          moneyInput=int(input(f"Please insert a £10 (10) or £20 (20) note. You still have to pay {tempTotal-tempTotal-tempTotal} £"))
          notDone = False
        except ValueError:
          print("Has to be a number")  
      if moneyInput == 10 or moneyInput == 20:
        tempTotal = tempTotal + moneyInput
      else:
        print("Not a valid coin. Please input 10 or 20")
  return tempTotal

def CarPass(parkPass):
  if parkPass == "y":
    print("Output parking pass")
    sleep(1)

while not_ended:
  if uses < 500:
    start = input(f"Welcome to Copington Adventure Theme Park! The ticket prices are £{adultPrice} for Adults, £{childPrice} for children and £{seniorPrice} for Seniors. Wristbands are £{wristbandPrice}. We have {500-uses} spaces left. Press enter to start or type SHUT DOWN to shut down.").lower()
    if start == "shut down":
      system('clear')
      print("Shutting down...")
      sleep(5)
      system('clear')
      not_ended = False
    else:
      adultTicket = TicketAdult()
      if adultTicket == 1774522:
        tempPrices = Admin()
        adultPrice = tempPrices[0]
        childPrice = tempPrices[1]
        seniorPrice = tempPrices[2]
        wristbandPrice = tempPrices[3]
        print("Adult prices are",adultPrice)
        print("Child prices are",childPrice)
        print("Senior prices are",seniorPrice)
        print("Wristband prices are",wristbandPrice)
      else:
        childTicket = TicketChild()
        seniorTicket = TicketSenior()
        if 500 < uses+adultTicket+childTicket+seniorTicket:
          print("Not enough spaces")
        else:
          wristbandAmmount = AmmountWristband()
          Surname = SurnameInput()
          parkPass = ParkPass()
          totalPrice = CostCalculator(adultTicket,adultPrice,childTicket,childPrice,seniorTicket,seniorPrice,wristbandAmmount,wristbandPrice)
          change = Payment(0-totalPrice)
          print(f"Finished with £{change} change.")
          sleep(5)
          CarPass(parkPass)
          print("Output tickets")
          sleep(1)
          print("Thank you for your purchase, Mr",Surname)
          uses = uses + adultTicket + childTicket + seniorTicket
          sleep(10)
          system('clear')
  else:
    print("Maximum capacity reached")
    not_ended = False