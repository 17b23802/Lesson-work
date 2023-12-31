from time import sleep
from random import randint, choice

correct = 0
print("Welcome to joke machine! You have to guess the punchline to the following jokes!")
one = input("What is pink and fluffy?").lower()
if one == "pink fluff":
  print("You got it!")
  correct = correct + 1
elif one == "pink sheep" or "cotton candy":
  print("Close but no cigar")
  sleep(2)
  print("Because smoking can KILL")
else:
  print("Sorry, that's incorrect, the punchline was: pink fluff")
two = input("What is brown and sticky?").lower()
if two == "a brown stick" or "brown stick":
  print("You did it!")
  correct = correct + 1
elif two == "poo":
  print("You disgust me")
else:
  print("Sorry, that's incorrect, the punchline was: a brown stick")
three = input("What is black and white and red all over?").lower()
if three == "a newspaper" or "newspaper":
  print("You did it!")
  correct = correct + 1
elif three == "a sunburnt penguin" or "sunburnt penguin" or "bleeding penguin" or "a bleeding penguin" or "a sunburnt zebra" or "sunburnt zebra" or "bleeding zebra" or "a bleeding zebra":
  print("P.E.T.A, I'd like to file an animal abuse case.")
else:
  print("Sorry, that's incorrect, the punchline was: a newspaper")
print("Your total score was",correct)
if correct == 3:
  print("You are now part of an elite group of society!")
  sleep(3)
  print("(unless you went through more than once. If you did you're going to grow up to be a criminal)")
elif correct == 2:
  print("Close but you're still stupid")
elif correct == 1:
  print("Ya pretty bad kid")
else:
  print("git gud n00b")