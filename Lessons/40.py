from time import sleep
from termcolor import colored
from random import randint
from os import system

file = open("Files/scores.csv", "r")
data = []
for line in file:
    line = line.strip()
    data.append(line)
file.close()
x=1
y=0
lowest=data[1]
highest=data[1]
while x<len(data):
  if int(data[x])<int(lowest):
    lowest=data[x]
  elif int(data[x])>int(highest):
    highest=data[x]
  y=y+int(data[x])
  x=x+1
print("The lowest number is",lowest)
print("The highest number is",highest)
print("The average is",y/(len(data)-1))

file=open("Files/names.csv","r")
data=[]
letter=input("Enter the first letter of the name: ").upper()
for line in file:
  if line[0].upper()==letter:
    data.append(line)
x=0
while x<len(data):
  print(data[x].strip())
  x=x+1

file = open("Files/players.csv", "r")
data = []
player=input("Enter the player")
for line in file:
  line = line.strip()
  line = line.split(",")
  data.append(line)
score=0
x=0
while x<len(data):
  if data[x][0]==player:
    score=data[x][1]
  x=x+1
if score==0:
  print("No value")
else:
  print(f"Their score is {score}")
file.close()

file=open("Files/weatherdata.csv")
data=[]
for line in file:
  line = line.strip()
  line = line.split(",")
  data.append(line)
highest=0
data.pop(0)
for item in data:
  when1=item[0]
  item.pop(0)
  for item in item:
    if float(item) > float(highest):
      highest=item
      when=when1
print(f"The highest rainfall was {highest} at {when}")
  