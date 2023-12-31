from time import sleep
from random import randint
from os import system

stored_word = "password"
word = ""
word_mismatch = stored_word != word
attempts = 5

print("The word has",len(stored_word),"letters")
while word_mismatch:
    if attempts == 0:
      word_mismatch = False
      attempts=-2
    else:
      print(f"Guess the word, you have {attempts} tries left:")
      word = input()
      if len(word)==1:
        count=0
        for letter in stored_word:
          if letter == word:
            count = count + 1
        print("It has the letter",word,"",count,"times")
      else:
        if stored_word == word:
          word_mismatch = False
        else:
          attempts = attempts - 1
          if attempts == 4:
            print("The first letter of the word is",stored_word[0])
          if attempts == 2:
            print("The last letter of the word is",stored_word[len(stored_word)-1])

if attempts>-2:
  print("Correct, you win")
else:
  print("Incorrect, you lose!")
sleep(5)
system('clear')

not_done = True
while not_done:
  letterCount=input("What character would you like to test for?")
  if len(letterCount) == 1:
    not_done = False
  else:
    print("It has to be a single character")
word = "sheep"
count = 0

for letter in word:
    if letter == letterCount:
        count = count + 1

print(count)
