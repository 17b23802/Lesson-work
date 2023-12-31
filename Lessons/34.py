from time import sleep
from random import randint, shuffle
from termcolor import colored
from os import system

suits = ["♡", "♦", "♣", "♠"]
deck = []
p1=[]
p2=[]
for suit in suits:
  for card in range(1,14):
    if card==1:
      value="A"
    elif card==11:
      value="J"
    elif card==12:
      value="Q"
    elif card==13:
      value="K"
    else:
      value=str(card)
    deck.append(value+suit)
shuffle(deck)
p1=str(deck[:int(len(deck)/2)]).replace("♡",colored("♡",'red')).replace("♦",colored("♦",'red'))
p2=str(deck[int(len(deck)/2):]).replace("♡",colored("♡",'red')).replace("♦",colored("♦",'red'))
print(p1)
print(p2)