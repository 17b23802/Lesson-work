from termcolor import colored
from random import shuffle, randint
from os import system
from time import sleep

questions = []
not_done = True
x = 0
subject = "maths"#input(colored("Which subject are you revising today? ",'blue')).lower()
#Add physics textbook sections and Computing topic list 
system('clear')
file=open(f"Revision/{subject}.txt","r").read()
lines=[]
file=file.split('\n')
while not_done:
  incorrect=open("Revision/Incorrect.txt","a")
  print(file[0])
  number=randint(1,len(file)-1)
  print(number)
  response=input(file[number]+"\n")
  if response == "done":
    not_done=False
  elif response != "":
    incorrect.write(file[number]+": "+ response+"\n")
    incorrect.close()
  system('clear')
print("Done")

""" Sadly broken but I will keep it for legacy
try:
  file=open(f"{input().lower()}.txt","r")
  print(f"{input().lower()}")
#Remake Incorrect test
except:
  f1 = open("Revision/computing.txt", "r")
  f2 = open("Revision/maths.txt", "r")
  f3 = open("Revision/physics.txt", "r")
  f1a = []
  f2a = []
  f3a = []
  for line in f1:
    line = line.rstrip()
    f1a.append(line)
  for line in f2:
    line = line.rstrip()
    f2a.append(line)
  for line in f3:
    line = line.rstrip()
    f3a.append(line)
  file = f1a + f2a + f3a
  print(
    "No valid input given, the program will default to all subjects given")
incorrect = open("Incorrect.txt", "a")
while not_done:
  use = file.split("\n")[randint(0, len(file.split("\n")) - 1)].split(",")
  if input(f"{use[0]} ") == "":
    print("Note: Does not work due to repl's console being too small")
    for item in use[1].split(" "):
      print(item)
    input()
    #input(use[1])
    system('clear')
"""