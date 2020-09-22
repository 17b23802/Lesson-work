from time import sleep
from random import randint
x = int(input("Which lesson? "))
#Printus deletus = 100
#Bingo = 150

if x == 5:
  print("Hello my name is Susan from space")
  print("What is your name?")
  name = input()
  print(f"Hello {name}. I am from the year 2210 and I am 20 years old")
  print("How old are you?")
  age = int(input())
  future_age=age+2210-2020
  print(f"Wow, by 2210 you will be {future_age}, that is really old!")
  print("What type of music are you into?")
  music = input()
  print(f"I have not heard of {music}")


if x == 4:
  noun=input("Input Noun")
  verb=input("Input verb")
  adjective=input("Input adjective")
  adverb=input("Input adverb")
  insert4thThingHere=input("insert 4th thing")
  print(f"The {adjective} {noun} decided to {verb} and they did it {adverb}. {insert4thThingHere}.")

  #try:
  #   tryexceptnumber=int(input("Enter a number"))
  #except:
  #  tryexceptnumber=int(input("Not an interger, try again"))
  print("What is your first initial?")
  initial = input()
  print("What is your surname")
  surname = input()
  print("What is your age?")
  age = int(input())
  print("Do you like marmite? Yes or No")
  marmite = input()
  likes_marmite = marmite == "Yes"
  decades = float(age / 10)
  print(f"Well hello {initial} {surname}.")
  print(f"It is {likes_marmite} that you like marmite.")
  print(f"This is probably because you are {decades} decades old")


if x == 150:
  bingo = input(print("Make your number"))
  callednumbers = []

  def makeNumber():
    print("And the number is...")
    sleep(3)
    randomNumber = randint(1,100)
    while picknumber(0,randomNumber) == 1:
      randomNumber = randint(1,100)
      picknumber(0,randomNumber)
    callednumbers.append(randomNumber)
    End = input("Is ",randomNumber," the number?")
    if End == "yes":
      return 1
    else:
      return 0

  def picknumber(y,tempbingo):
    while y <= 100:
      y = y + 1
      if tempbingo == callednumbers(y):
        y = 1000

  while makeNumber() == 0:
    makeNumber
  


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