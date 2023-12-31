from time import sleep
from termcolor import colored
from random import randint
from os import system
file = open("Files/bnumbers.txt","r")
x=0
for line in file:
  x=x+int(line)

print(x)
print()

file1=open("Files/btranscript1.txt","r")
file2=open("Files/btranscript2.txt","r")
for line in file1:
  x=line.strip()
  print(x)
  print(file2.readline().strip())
def cipher(key):
    caesar = {" ":" "} #Blank dictionary
    x=65 #Starts at A in ascii
    while x < 91: #Ends at punctuation
      number=x+key #Starts with A + key
      while number>90: #If it's greater than Z
        number=number-26 #Take away the alphabet to take it back to A
      while number<65: #If it's under A
        number=number+26 #Add the alphabet to increase it to Z
      caesar[chr(x)]=chr(number) #Add x and number to the dictionary as characters
      x=x+1 #Increase the while loop
    return caesar #Returns the dictionary
ceasar=cipher(-2)
words2=""
for letter in x.upper(): #For every letter
  try:
    words2=words2+ceasar[letter] #Add the dictionary translated version of the letter to the string
  except: #If there's no reference for it (punctuation, space etc)
    words2=words2+letter #Add the unchanged letter
print(words2)
  