from termcolor import colored
from os import system

notDone=True
while notDone:
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
  
  not_done=True
  while not_done: #Makes sure encrypt or decrypt is typed
    try:
      encrypt=input("Do you want to encrypt or decrypt? ").lower()
      if encrypt=="encrypt"or encrypt=="decrypt":
        system('clear')
        not_done=False
      else:
        system('clear')
        print(colored("You have to type encrypt or decrypt",'red'))
    except:
      print("Please don't terminate the current command") #Stops people from inputting ctrl-c

  not_done=True
  while not_done:
    try: #Makes sure an interger is assigned
      key=int(input("What is the encryption key? "))
      if encrypt=="decrypt": #If you're decrypting make the number a negative
        key=-key
      not_done=False
    except:
      system('clear')
      print(colored("Has to be a number",'red'))
      
  ceasar=cipher(key) #Gets the dictionary
  not_done=True
  while not_done:
    try:
      words=input("What would you like to translate?").upper() #Uppercase input
      not_done=False
    except:
      print("Please don't terminate the current command") #Stops people from inputting ctrl-c
  words2="" #Assigns a blank string
  for letter in words: #For every letter
    try:
      words2=words2+ceasar[letter] #Add the dictionary translated version of the letter to the string
    except: #If there's no reference for it (punctuation, space etc)
      words2=words2+letter #Add the unchanged letter
  print(words2) #Print the crypted product
  not_done=True
  while not_done:
    try:
      repeat=input("Would you like to use the machine again? Y/N ").lower()
      if repeat=="y":
        not_done=False
      elif repeat=="n":
        notDone=False
        not_done=False
      else:
        system('clear')
        print(colored("The input has to be Y or N",'red'))
    except:
      print("Please don't terminate the current command") #Stops people from inputting ctrl-c
  system('clear')