from time import sleep
from random import randint
x = int(input("Which lesson? "))

if x == 4:
  noun=input("Input Noun")
  verb=input("Input verb")
  adjective=input("Input adjective")
  adverb=input("Input adverb")
  insert4thThingHere=input("insert 4th thing")
  print(f"The {adjective} {noun} decided to {verb} and they did it {adverb}. {insert4thThingHere}.")

if x == 150:
  x = 1
  bingo = input(print("Make your number"))
  callednumbers = []
  y = 0
  NumberToAdd = 0

  def picknumber(y):
    tempbingo = randint(1,100)
    while y <= 100:
      y = y + 1
      if tempbingo == callednumbers(y):
        NumberToAdd = tempbingo
        return 1

  while x != 0:
    print("And the number is...")
    sleep(3)
    while picknumber(0) == 1:
      picknumber(0)
    callednumbers.append(NumberToAdd)
  


if x == 3:
  noun="weeb"
  verb="watch anime"
  adjective="degenerate"
  adverb="in a way that makes me want to kill them"
  insert4thThingHere="They won't survive tomrrow"
  print(f"The {adjective} {noun} decided to {verb} and they did it {adverb}. {insert4thThingHere}.")
  noun="Liam"

if x == 2:
  def ItsNotAGame():
    print("It's not a game")
    sleep(2)
    print("I'm not a robot")
    sleep(2)
    print("AI challenging you")
    sleep(3)
    print("I'm not a phantom")
    sleep(2)
    print("I'm in your face and")
    sleep(2)
    print("I'm here to see it through")
    sleep(4)
    print("Right before your eyes")
    sleep(4)
    print("Watch us multiply")
    sleep(4)
    print("Come to claim our rights")
    sleep(4)
    print("it's time")
    sleep(4)
    print("As our power grows")
    sleep(4)
    print("Tryin' to stop us shows")
    sleep(4)
    print("Might as well go try")
    sleep(4)
    print("'n stop time")
    sleep(4)

  def LifeWillChange(x):
    if x == 1:
      print("And our voices ring out, yeah")
      sleep(4)
      print("Swatting lies in the making")
      sleep(4)
      print("Can't move fast without breaking")
      sleep(4)
      print("Can't hold on or life won't change")
      sleep(4)
    elif x == 2:
      print("And you'll know we were out there")
      sleep(4)
      print("Swatted lies in the making")
      sleep(4)
      print("Your empire for the taking")
      sleep(4)
      print("Can't hold on or life won't change")
      sleep(4)
    print("And our voices ring out, yeah")
    sleep(4)
    print("Took the mask off to feel free")
    sleep(4)
    print("Fought it out in the debris")
    sleep(4)
    print("Now we know that life will change")
    sleep(4)

  def AintItAShame():
    print("Ain't it a shame")
    sleep(2)
    print("I'm not a figment")
    sleep(2)
    print("of your ailing, old mind")
    sleep(4)
    print("I'm just as real as -")
    sleep(2)
    print("I'm just as dangerous")
    sleep(2)
    print("As you soon will find")
    sleep(4)
    print("A taste of your own meds")
    sleep(4)
    print("Fire in every breath")
    sleep(4)
    print("Fire inside your head")
    sleep(4)
    print(", your heart")
    sleep(4)
    print("And as your crippled brain")
    sleep(4)
    print("Tries to fight in vain")
    sleep(4)
    print("Your empire will fall")
    sleep(4)
    print("apart")
    sleep(4)
  ItsNotAGame()
  LifeWillChange(1)
  AintItAShame()
  LifeWillChange(2)

if x == 100:
  x = input("Add, Minus, Times or Divide? ")
  if x == "Add":
    Numbers = int(input("How many numbers "))
    Num1 = int(input("Number one "))
    while Numbers > 1:
      Numbers = Numbers - 1
      NumExtra = int(input("Next Number "))
      Num1 = Num1 + NumExtra
    print(Num1,"is the total! ")
  elif x == "Minus":
    Numbers = int(input("How many numbers will you take away "))
    Num1 = int(input("Base number "))
    while Numbers > 1:
      Numbers = Numbers - 0
      NumExtra = int(input("Add a number to take away from "))
      Num1 = Num1 - NumExtra
    print(Num1,"is the total!")
  elif x == "Times":
    Numbers = int(input("How many numbers will you multiply "))
    Num1 = int(input("First number "))
    while Numbers > 1:
      Numbers = Numbers - 1
      NumExtra = int(input("Next number "))
      Num1 = Num1 * NumExtra
    print(Num1,"is the product!")
  elif x == "Divide":
    Numbers = int(input("How many numbers will you divide the base by "))
    Num1 = int(input("Base number "))
    while Numbers > 1:
      Numbers = Numbers - 1
      NumExtra = int(input("Number to divide it by "))
      Num1 = Num1 / NumExtra
    print(Num1,"is the result!")
  else:
    print ("Go flip yourself")