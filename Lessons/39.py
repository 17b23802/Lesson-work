from time import sleep
from termcolor import colored
from random import randint
from os import system

file = open("Files/players.txt", "w")
a=input("Enter the first player name")
b=input("Enter the second player name")
c=input("Enter the third player name")
d=input("Enter the fourth player name")
file.write(f"{a}\n{b}\n{c}\n{d}")
file.close()
file=open("Files/players.txt","r")
for line in file:
  print(line.strip())
file.close()

option=int(input("Would you like to 1. add, 2. divide, 3. multiply or 4. subtract? Enter 1 to 4"))
num1=int(input("Enter your first number"))
num2=int(input("Enter your second number"))
if option==1:
  answer=num1+num2
elif option==2:
  answer=num1/num2
elif option==3:
  answer=num1*num2
elif option==4:
  answer=num1-num2
else:
  while True:
    print("Invalid input")
    system('clear')
file=open("Files/calculation.txt","w")
file.write(str(answer))
file.close()
file=open("Files/calculation.txt","r")
for line in file:
  print(line.strip())
file.close()

score=input("Enter your latest score:")
timestamp = "Importing datetime made this take too long to load"
newscore = (f"\n{score} recorded at: {timestamp}")
file = open("Files/scores.txt", "a")
file.write(newscore)
file.close()

file=open("Files/romeojulliet.txt","r")
a=0
for line in file:
  for letter in line:
    if letter=="a":
      a=a+1
file.close()
file=open("Files/romeojulliet.txt","a")
file.write(f"\n\nLetter: a\nOccurences= {a}")