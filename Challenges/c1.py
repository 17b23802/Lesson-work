from time import sleep
from random import randint, choice
attempts = 1
number = str(randint(1000,9999))
def guess_the_number(number):
  numbers_right = 0
  guessed = str(input("Guess a four digit number: "))
  if guessed == number:
    print("You did it!")
    return 1
  else:
    if number[0] == guessed[0]:
      numbers_right = numbers_right + 1
    if number[1] == guessed[1]:
      numbers_right = numbers_right + 1
    if number[2] == guessed[2]:
      numbers_right = numbers_right + 1
    if number[3] == guessed[3]:
      numbers_right = numbers_right + 1
    print("Wrong, you got",numbers_right,"numbers right though")
    return 2

correct = guess_the_number(number)
while correct == 2:
  attempts = attempts + 1
  correct = guess_the_number(number)
sleep(3)
print("You took",attempts,"attempts")