from time import sleep
from random import randint, choice

number = randint(1,10)
guesses = 1
print("Guess a number between 1 and 10")
guess = int(input())
while guess != number or guesses > 3:
  print("Incorrect")
  sleep(1)
  if guess > number:
    print("The number is lower than your guess")
  else:
    print("The number is higher than your guess")
  print("Guess a number between 1 and 10")
  guesses = guesses + 1
  guess = int(input())
if guesses > 3:
  print("You took too many tries...")
else:
  print(Fore.GREEN + "Correct")
  if guesses == 1:
    print(Fore.GREEN + "You guessed it on the first try!")
  else:
    print(Fore.RED + "You guessed it in",guesses,"tries!")