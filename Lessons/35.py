from random import randint
from os import system

board = [["1", "2", "3"],
        ["4", "5", "6"],
        ["7", "8", "9"]]
not_done=True
won=False
P1=0
P2=0
inputs=0
def instructions(): #Runs a single input for the user to read and finish at their own pace
  input("""Welcome to noughts and crosses
--------------------------------
Instructions:

This is a  2 player game
The first player will be noughts
The second player will be crosses
The game is presented in a grid
 1 │ 2 │ 3
───┼───┼───
 4 │ 5 │ 6 
───┼───┼───
 7 │ 8 │ 9 
To choose a position for your piece, enter the location number
Press enter to continue""")
  system('clear')

def move(board, player):
  notdone=True
  while notdone:
    if player == "c": #Computer check
      position=str(randint(1,9))
    else:
      position=input(f"Enter the position on the board player {player} wants to play: ")
    if position=="X" or position=="O": #Stops overlap
      print("You can't play on a space that has already been played on")
    elif position=="":
      print("You need to input a position")
    else:
      notDone=True
      board2=board 
      coordinates1=0
      coordinates2=0
      failed=False
      while notDone:
        try: #Sets a blank value to coordinates if they exist
          index = board2[coordinates1][coordinates2].index(position)
          board2[coordinates1][coordinates2]=player
          notDone=False
        except: #Throws an error defining index if it doesn't exist
          if coordinates2>1: #Sets it to look in the next avaliable coordinate
            coordinates2=0
            coordinates1=coordinates1+1
          else: #If the first coordinate can't increase anymore
            coordinates2=coordinates2+1
          if coordinates1>2: #If over the maximum boundry of coordinates, fail and end the loop
            failed=True
            notDone=False
      if failed==False: 
        board=board2 #Sets the main board to the temp board
        system('clear')
        displayboard(board) #Always displays the board
        notdone=False
      else:
        print("Needs to be an unnocupied number")

def displayboard(board): #Displaying the board
  print(" ", board[0][0], "│", board[0][1], "│", board[0][2])
  print(" ───┼───┼───")
  print(" ", board[1][0], "│", board[1][1], "│", board[1][2])
  print(" ───┼───┼───")
  print(" ", board[2][0], "│", board[2][1], "│", board[2][2])

def check_win(board, player): #Checks all combinations for winning with the passed player
  won = False #Makes any definition for won
  if board[0][0] == player and board[1][0] == player and board[2][0] == player:
    won = True
  if board[0][1] == player and board[1][1] == player and board[2][1] == player:
    won = True
  if board[0][2] == player and board[1][2] == player and board[2][2] == player:
    won = True
  if board[0][0] == player and board[0][1] == player and board[0][2] == player:
    won = True
  if board[1][0] == player and board[1][1] == player and board[1][2] == player:
    won = True
  if board[2][0] == player and board[2][1] == player and board[2][2] == player:
    won = True
  if board[0][0] == player and board[1][1] == player and board[2][2] == player:
    won = True
  if board[2][0] == player and board[1][1] == player and board[0][2] == player:
    won = True
  return won #If it gets set to True it passes True, otherwise it passes false

instructions()
not__done=True
while not__done: #Computer check
  computer = input("Do you want to go against a player (p) or a computer (c)?").lower()
  if computer == "p" or computer == "c":
    previous=computer
    not__done=False
  else:
    system('clear')
    print("You have to input c or p")
displayboard(board)
while not_done:
  if won: #If game is won
    print(f"Player 1 has won {P1} times and Player 2 has won {P2} times!")
    notdone=True
    while notdone:
      repeat=input("Do you want to play again? Y/N ").lower()
      if repeat == "y": #Reset the win, reset the board, reset the inputs, clear the text, ask for computer or player
        won=False
        board = [["1", "2", "3"],
          ["4", "5", "6"],
          ["7", "8", "9"]]
        inputs=0
        system('clear')
        not__done=True
        while not__done:
          computer = input("Do you want to go against a player (p) or a computer (c)?").lower()
          if computer == "p" or computer == "c":
            if computer!=previous:
              P1=0
              P2=0
            previous=computer
            not__done=False
          else:
            system('clear')
            print("You have to input c or p")
        displayboard(board)
        notdone=False
      elif repeat == "n": #Ends the not done statements
        print("End")
        not_done=False
        notdone=False
      else:
        print("Not a valid input")
  else:
    move(board,"X") #Move, add an input, check if they've won
    inputs=inputs+1
    if check_win(board,"X")==True:
      print("Player 1 wins")
      won=True
      P1=P1+1
    elif inputs==9: #If max number of inputs (has to be done after player 1 for an odd number)
      print("It's a draw!")
      won=True
    else:
      if computer == "c":
        move(board,"c")
      else:
        move(board,"O")
      inputs=inputs+1
      if check_win(board,"O") or check_win(board,"c"):
        print("Player 2 wins")
        won=True
        P2=P2+1