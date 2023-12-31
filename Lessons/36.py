from time import sleep
from termcolor import colored
from random import randint
from os import system


books=[]
not_done=True
while not_done:
  book = {"title": "",
          "author":"",
          "genre": "", }
  
  book["title"] = input("What's the title of the book?")
  book["author"] = input("Who's the author of the book?")
  book["genre"] = input("What's the genre of the book?")
  books.append(book)
  if input("Would you like to add another book? Y/N").lower()=="n":
    not_done=False

print(books)

players = []

add_players = True
while add_players:
    print("Enter a username:")
    username = input()
    print("Enter a password:")
    password = input()
    print("Enter a score:")
    score = input()
    print("Enter the user's highest score:")
    highest_score=input()

    player = {"username" : username,
              "password" : password,
              "score" : score,
              "highest_score" : highest_score}

    players.append(player)

    print("Would you like to add another player? Y/N")
    answer = input().upper()
    if answer == "N":
        add_players = False

print(players[0]["password"])
print(players[int(input("Which record would you like to access?"))][input("Which record would you like to access?")])