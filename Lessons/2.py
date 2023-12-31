from time import sleep
from random import randint, choice

noun=input("Input Noun")
verb=input("Input verb")
adjective=input("Input adjective")
adverb=input("Input adverb")
insert4thThingHere=input("insert 4th thing")
print(f"The {adjective} {noun} decided to {verb} and they did it {adverb}. {insert4thThingHere}.")
print("What is your first initial?")
initial = input()
print("What is your surname")
surname = input()
print("What is your age?")
age = int(input())
print("Do you like marmite? Yes or No")
marmite = input()
likes_marmite = marmite == "Yes"
decades = float(age / 10)
print(f"Well hello {initial} {surname}.")
print(f"It is {likes_marmite} that you like marmite.")
print(f"This is probably because you are {decades} decades old")