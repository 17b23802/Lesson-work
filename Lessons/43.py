from random import randint
from os import system
exit=True #gettothechoppa.mp4

def instructions(): #Runs a single input for the user to read and finish at their own pace
  input("""Welcome to Battle Boats
--------------------------------
Instructions:

This is a singleplayer game against a computer
You will place 5 boats on a grid and then try to work out where the computer's boats are by hitting a target on their board.
The game is presented in a grid
 │ A │ B │ C │ D │ E │ F │ G │ H
─┼───┼───┼───┼───┼───┼───┼───┼───
1│   │   │   │   │   │   │   │
─┼───┼───┼───┼───┼───┼───┼───┼───
2│   │   │   │   │   │   │   │
─┼───┼───┼───┼───┼───┼───┼───┼───
3│   │   │   │   │   │   │   │
─┼───┼───┼───┼───┼───┼───┼───┼───
4│   │   │   │   │   │   │   │
─┼───┼───┼───┼───┼───┼───┼───┼───
5│   │   │   │   │   │   │   │
─┼───┼───┼───┼───┼───┼───┼───┼───
6│   │   │   │   │   │   │   │
─┼───┼───┼───┼───┼───┼───┼───┼───
7│   │   │   │   │   │   │   │
─┼───┼───┼───┼───┼───┼───┼───┼───
8│   │   │   │   │   │   │   │
When asked to place a coordinate, you need to use a letter then a number to show where you want to input. For example A7 would be:
 │ A │ B │ C │ D │ E │ F │ G │ H
─┼───┼───┼───┼───┼───┼───┼───┼───
1│   │   │   │   │   │   │   │
─┼───┼───┼───┼───┼───┼───┼───┼───
2│   │   │   │   │   │   │   │
─┼───┼───┼───┼───┼───┼───┼───┼───
3│   │   │   │   │   │   │   │
─┼───┼───┼───┼───┼───┼───┼───┼───
4│   │   │   │   │   │   │   │
─┼───┼───┼───┼───┼───┼───┼───┼───
5│   │   │   │   │   │   │   │
─┼───┼───┼───┼───┼───┼───┼───┼───
6│   │   │   │   │   │   │   │
─┼───┼───┼───┼───┼───┼───┼───┼───
7│ X │   │   │   │   │   │   │
─┼───┼───┼───┼───┼───┼───┼───┼───
8│   │   │   │   │   │   │   │
Press enter to continue""")
  system('clear')

def display_board(board): #Displaying the board
  print("  │ A │ B │ C │ D │ E │ F │ G │ H")
  print(" ─┼───┼───┼───┼───┼───┼───┼───┼───")
  print("1 │", board[0][0], "│", board[0][1], "│", board[0][2], "│", board[0][3], "│", board[0][4], "│", board[0][5], "│", board[0][6], "│", board[0][7])
  print(" ─┼───┼───┼───┼───┼───┼───┼───┼───")
  print("2 │", board[1][0], "│", board[1][1], "│", board[1][2], "│", board[1][3], "│", board[1][4], "│", board[1][5], "│", board[1][6], "│", board[1][7])
  print(" ─┼───┼───┼───┼───┼───┼───┼───┼───")
  print("3 │", board[2][0], "│", board[2][1], "│", board[2][2], "│", board[2][3], "│", board[2][4], "│", board[2][5], "│", board[2][6], "│", board[2][7])
  print(" ─┼───┼───┼───┼───┼───┼───┼───┼───")
  print("4 │", board[3][0], "│", board[3][1], "│", board[3][2], "│", board[3][3], "│", board[3][4], "│", board[3][5], "│", board[3][6], "│", board[3][7])
  print(" ─┼───┼───┼───┼───┼───┼───┼───┼───")
  print("5 │", board[4][0], "│", board[4][1], "│", board[4][2], "│", board[4][3], "│", board[4][4], "│", board[4][5], "│", board[4][6], "│", board[4][7])
  print(" ─┼───┼───┼───┼───┼───┼───┼───┼───")
  print("6 │", board[5][0], "│", board[5][1], "│", board[5][2], "│", board[5][3], "│", board[5][4], "│", board[5][5], "│", board[5][6], "│", board[5][7])
  print(" ─┼───┼───┼───┼───┼───┼───┼───┼───")
  print("7 │", board[6][0], "│", board[6][1], "│", board[6][2], "│", board[6][3], "│", board[6][4], "│", board[6][5], "│", board[6][6], "│", board[6][7])
  print(" ─┼───┼───┼───┼───┼───┼───┼───┼───")
  print("8 │", board[7][0], "│", board[7][1], "│", board[7][2], "│", board[7][3], "│", board[7][4], "│", board[7][5], "│", board[7][6], "│", board[7][7])

def generate_board(player):
  file=open(f"Files/battleboat{player}.csv","w")
  board=[[" ", " ", " ", " ", " ", " ", " ", " "],
            [" ", " ", " ", " ", " ", " ", " ", " "],
            [" ", " ", " ", " ", " ", " ", " ", " "],
            [" ", " ", " ", " ", " ", " ", " ", " "],
            [" ", " ", " ", " ", " ", " ", " ", " "],
            [" ", " ", " ", " ", " ", " ", " ", " "],
            [" ", " ", " ", " ", " ", " ", " ", " "],
            [" ", " ", " ", " ", " ", " ", " ", " "]]
  i=0
  if player=="P1":
    while i<5:
      if i<3:
        display_board(board)
      not_done=True
      while not_done:
        try:
          coordinate1=input("What coordinate would you like to place a boat in\n").upper()
          if board[int(coordinate1[1])-1][int(ord(coordinate1[0])-65)]==" ":
            if coordinate1[1]=="0":
              coordinate1[-1]="intentional error"
            board[int(coordinate1[1])-1][int(ord(coordinate1[0])-65)]=str(i+1)
            system('clear')
            not_done=False
            if i>=2:
              display=True
              not__done=True
              while not__done:
                if i<4:
                  if display:
                    display_board(board)
                    display=False
                  coordinate2=input("Where would you like to extend the boat to (input a coordinate next to the current boat)? You can also type cancel to remove the boat\n").upper()
                  direction=" "
                else:
                  if display:
                    display_board(board)
                    display=False
                  direction=input("Would you like to extend the boat 2 values up, down, left or right? You can also type cancel to remove the boat\n").lower()
                try:
                  if coordinate2=="CANCEL" or direction[0]=="c": #Cancel command
                    board[int(coordinate1[1])-1][int(ord(coordinate1[0])-65)]=" " #Removes the first boat
                    not__done=False #Stops the extention
                    not_done=True #Reenables the boat placing command
                  elif i>=4: #If this is boat 5
                    try:
                      if direction[0]=="d": #Down
                        if board[int(coordinate1[1])][int(ord(coordinate1[0])-65)]==" " and board[int(coordinate1[1])+1][int(ord(coordinate1[0])-65)]==" ":
                          board[int(coordinate1[1])][int(ord(coordinate1[0])-65)]=str(i+1)
                          board[int(coordinate1[1])+1][int(ord(coordinate1[0])-65)]=str(i+1) 
                          not__done=False #End the loop
                        else:
                          print("These values are taken or off the board")
                      elif direction[0]=="u": #Up
                        if int(coordinate1[1])-3>=0 and board[int(coordinate1[1])-2][int(ord(coordinate1[0])-65)]==" " and board[int(coordinate1[1])-3][int(ord(coordinate1[0])-65)]==" ": #If it stays on the board and both spaces are empty
                          board[int(coordinate1[1])-2][int(ord(coordinate1[0])-65)]=str(i+1)
                          board[int(coordinate1[1])-3][int(ord(coordinate1[0])-65)]=str(i+1) 
                          not__done=False #End the loop
                        else:
                          print("These values are taken or off the board")
                      elif direction[0]=="l": #Left
                        if int(ord(coordinate1[0])-67)>=0 and board[int(coordinate1[1])-1][int(ord(coordinate1[0])-66)]==" " and board[int(coordinate1[1])-1][int(ord(coordinate1[0])-67)]==" ":
                          board[int(coordinate1[1])-1][int(ord(coordinate1[0])-66)]=str(i+1)
                          board[int(coordinate1[1])-1][int(ord(coordinate1[0])-67)]=str(i+1) 
                          not__done=False #End the loop
                        else:
                          print("These values are taken or off the board")
                      elif direction[0]=="r": #Right
                        if board[int(coordinate1[1])-1][int(ord(coordinate1[0])-64)]==" " and board[int(coordinate1[1])-1][int(ord(coordinate1[0])-63)]==" ":
                          board[int(coordinate1[1])-1][int(ord(coordinate1[0])-64)]=str(i+1)
                          board[int(coordinate1[1])-1][int(ord(coordinate1[0])-63)]=str(i+1)
                          not__done=False #End the loop
                        else:
                          print("These values are taken or off the board")
                      else:
                        print("That's not a direction")
                    except:
                      print("These values are taken or off the board")
                  elif int(coordinate2[1])-1<0 or int(coordinate2[1])>8 or int(ord(coordinate1[0]))-65<0 or int(ord(coordinate1[0]))-65>8:
                    print("Coordinate out of range")
                  elif str(int(coordinate1[1])-2)+str(int(ord(coordinate1[0])-65))==str(int(coordinate2[1])-1)+str(int(ord(coordinate2[0])-65)) or str(int(coordinate1[1]))+str(int(ord(coordinate1[0]))-65)==str(int(coordinate2[1])-1)+str(int(ord(coordinate2[0]))-65) or str(int(coordinate1[1])-1)+str(int(ord(coordinate1[0]))-65)==str(int(coordinate2[1])-1)+str(int(ord(coordinate2[0]))-66) or str(int(coordinate1[1])-1)+str(int(ord(coordinate1[0]))-65)==str(int(coordinate2[1])-1)+str(int(ord(coordinate2[0]))-64): #If up, down, right or left coordinate is the first coordinate
                    board[int(coordinate2[1])-1][int(ord(coordinate2[0])-65)]=str(i+1)
                    not__done=False #End the loop
                  else:
                    print("Please input an empty coordinate next to the current boat")
                except:
                  print("Can't do that")
              system('clear')
              display_board(board)
          else:
            print("You have already placed in this coordinate")
        except:
          print("Invalid coordinate")
      i+=1
  elif player=="P2":
    while i<5:
      not_done=True
      while not_done:
        coordinate1=chr(randint(65,72))+str(randint(1,8)) #Random coordinate
        if board[int(coordinate1[1])-1][int(ord(coordinate1[0])-65)]==" ": #If nothing in the space
          i+=1
          board[int(coordinate1[1])-1][int(ord(coordinate1[0])-65)]=str(i) #Place a boat
          not_done=False
          if i>2 and i<5: #If 2 boats have been previously placed and no more than 4 have
            if randint(1,2)==1: #Random if extention goes left or up (down and right isn't needed)
              try:
                if int(ord(coordinate1[0])-66)>=0 and board[int(coordinate1[1])-1][int(ord(coordinate1[0])-66)]==" ": #If the coordinate going left one fits on the board and is empty
                  board[int(coordinate1[1])-1][int(ord(coordinate1[0])-66)]=str(i) #Place a boat in the space one left
                else:
                  i-=1 #Remove a counter
                  board[int(coordinate1[1])-1][int(ord(coordinate1[0])-65)]=" " #Remove the original boat
              except: #If off the board
                i-=1 #Remove a counter
                board[int(coordinate1[1])-1][int(ord(coordinate1[0])-65)]=" " #Remove the original boat
            else:
              try:
                if int(coordinate1[1])-2>=0 and board[int(coordinate1[1])-2][int(ord(coordinate1[0])-65)]==" ": #If the coordinate going up one fits on the board and is empty
                  board[int(coordinate1[1])-2][int(ord(coordinate1[0])-65)]=str(i) #Place a boat 1 space up
                else:
                  i-=1 #Remove a counter
                  board[int(coordinate1[1])-1][int(ord(coordinate1[0])-65)]=" " #Remove the original boat
              except: #If it can't be placed there
                i-=1 #Remove a counter
                board[int(coordinate1[1])-1][int(ord(coordinate1[0])-65)]=" " #Remove the original boat
          elif i==5: #If it's the final boat
            if randint(1,2)==1: #Left and right or up and down
              try:
                if board[int(coordinate1[1])-1][int(ord(coordinate1[0])-66)]==" " and board[int(coordinate1[1])-1][int(ord(coordinate1[0])-64)]==" " and int(ord(coordinate1[0])-66)>=0 and board[int(coordinate1[1])-1][int(ord(coordinate1[0])-66)]==" " and int(ord(coordinate1[0])-64)>=0 and board[int(coordinate1[1])-1][int(ord(coordinate1[0])-64)]==" ": #If the spaces left and right are free
                  board[int(coordinate1[1])-1][int(ord(coordinate1[0])-66)]=str(i) #Place a boat in the space one left
                  board[int(coordinate1[1])-1][int(ord(coordinate1[0])-64)]=str(i) #Place a boat in the space one right
                else: #If it can't be placed there
                  i-=1 #Remove a counter
                  board[int(coordinate1[1])-1][int(ord(coordinate1[0])-65)]=" " #Remove the original boat
              except:
                i-=1 #Remove a counter
                board[int(coordinate1[1])-1][int(ord(coordinate1[0])-65)]=" " #Remove the original boat
            else:
              try:
                if board[int(coordinate1[1])-2][int(ord(coordinate1[0])-65)]==" " and board[int(coordinate1[1])][int(ord(coordinate1[0])-65)]==" " and int(coordinate1[1])-2>=0 and board[int(coordinate1[1])-2][int(ord(coordinate1[0])-65)]==" " and int(coordinate1[1])>=0 and board[int(coordinate1[1])-2][int(ord(coordinate1[0])-65)]==" ": #If the space above and below are free
                  board[int(coordinate1[1])-2][int(ord(coordinate1[0])-65)]=str(i) #Place a boat 1 space up
                  board[int(coordinate1[1])][int(ord(coordinate1[0])-65)]=str(i)#Place a boat 1 space down
                else: #If it can't be placed there
                  i-=1 #Remove a counter
                  board[int(coordinate1[1])-1][int(ord(coordinate1[0])-65)]=" " #Remove the original boat
              except: #If off the board
                i-=1 #Remove a counter
                board[int(coordinate1[1])-1][int(ord(coordinate1[0])-65)]=" " #Remove the original boat
  board_string=""
  for line in board:
    for item in line:
      board_string=board_string+item+","
    board_string=board_string+"\n"
  file.write(board_string)
  file.close()

def sink(board,player):
  not_done=True
  while not_done:
    if player=="P1":
      coordinate=input("Enter the coordinate you would like to shoot\n").upper()
      player2="P2"
    else:
      coordinate=chr(randint(65,72))+str(randint(1,8)) #Random coordinate
      player2="P1"      
      global CPU_Coordinate
      CPU_Coordinate="The enemy has shot "+coordinate
    try:
      if coordinate[1]=="0":
        print("You can't have coordinates ending with 0")
      elif board[int(coordinate[1])-1][int(ord(coordinate[0])-65)]=="1" or board[int(coordinate[1])-1][int(ord(coordinate[0])-65)]=="2" or board[int(coordinate[1])-1][int(ord(coordinate[0])-65)]=="3" or board[int(coordinate[1])-1][int(ord(coordinate[0])-65)]=="4" or board[int(coordinate[1])-1][int(ord(coordinate[0])-65)]=="5": #If a boat is found (number)
        if open(f"Files/battleboat{player2}.csv","r").read().count(board[int(coordinate[1])-1][int(ord(coordinate[0])-65)])==1: #If there's less than 1 of the number
          board_string=""
          for line in board:
            for item in line:
              if item !="\n":
                board_string=board_string+item+","
            board_string=board_string+"\n"
          if board[int(coordinate[1])-1][int(ord(coordinate[0])-65)]=="1": #If it's the first boat
            board_string=board_string.replace("1","S") #Replace the boat with sunk
          elif board[int(coordinate[1])-1][int(ord(coordinate[0])-65)]=="2": #If it's the second boat
            board_string=board_string.replace("2","S") #Replace the boat with sunk
          elif board[int(coordinate[1])-1][int(ord(coordinate[0])-65)]=="3": #If it's the third boat
            board_string=board_string.replace("C","S").replace("3","S") #Replace all shot sections of the boat with sunk
          elif board[int(coordinate[1])-1][int(ord(coordinate[0])-65)]=="4":#If it's the fourth boat
            board_string=board_string.replace("D","S").replace("4","S") #Replace all shot sections of the boat with sunk
          elif board[int(coordinate[1])-1][int(ord(coordinate[0])-65)]=="5":#If it's the fith boat
            board_string=board_string.replace("E","S").replace("5","S") #Replace all shot sections of the boat with sunk
        else: #If there's more if the boat left, replaces 3 with C or 4 with D or 5 with E
          if board[int(coordinate[1])-1][int(ord(coordinate[0])-65)]=="3":
            board[int(coordinate[1])-1][int(ord(coordinate[0])-65)]="C"
          elif board[int(coordinate[1])-1][int(ord(coordinate[0])-65)]=="4":
            board[int(coordinate[1])-1][int(ord(coordinate[0])-65)]="D"
          elif board[int(coordinate[1])-1][int(ord(coordinate[0])-65)]=="5":
            board[int(coordinate[1])-1][int(ord(coordinate[0])-65)]="E"
          board_string=""
          for line in board:
            for item in line:
              if item !="\n":
                board_string=board_string+item+","
            board_string=board_string+"\n"
        not_done=False
      elif board[int(coordinate[1])-1][int(ord(coordinate[0])-65)]==" ":
        board[int(coordinate[1])-1][int(ord(coordinate[0])-65)]="M"
        board_string=""
        for line in board:
          for item in line:
            if item !="\n":
              board_string=board_string+item+","
          board_string=board_string+"\n"
        not_done=False
      elif player=="P1": 
        print("You have already shot that coordinate")
    except:
      print("Invalid coordinate")
  file=open(f"Files/battleboat{player2}.csv","w") #Saves the game
  file.write(board_string)
  file.close()
  board=[] 
  for line in open(f"Files/battleboat{player2}.csv"): #Reads the transformed board_string and turns it into a list
    board.append(line.split(","))
  return board

while exit:
  not_done=True
  start=False
  CPU_Coordinate=""
  decision=input("""Choose an option:
1. New game
2. Resume game
3. Read the instructions
4. Exit
""")
  system("clear")
  try:
    if decision[0]=="1":
      generate_board("P1")
      generate_board("P2")
      start=True
    elif decision[0]=="2":
      try:
        if open(f"Files/battleboatP1.csv","r").read().find(",")==-1:
          print("A game has not been previously made")
        elif open(f"Files/battleboatP2.csv","r").read().find("1")==-1 and open(f"Files/battleboatP2.csv","r").read().find("2")==-1 and open(f"Files/battleboatP2.csv","r").read().find("3")==-1 and open(f"Files/battleboatP2.csv","r").read().find("4")==-1 and open(f"Files/battleboatP2.csv","r").read().find("5")==-1 or open(f"Files/battleboatP1.csv","r").read().find("1")==-1 and open(f"Files/battleboatP1.csv","r").read().find("2")==-1 and open(f"Files/battleboatP1.csv","r").read().find("3")==-1 and open(f"Files/battleboatP1.csv","r").read().find("4")==-1 and open(f"Files/battleboatP1.csv","r").read().find("5")==-1: #Makes sure no players have already won
          print("The previous game already ended")
        else:
          start=True
      except:
        print("A game has not been previously made")
    elif decision[0]=="3":
      instructions()
    elif decision[0]=="4":
      exit=False
    if start:
      P1=[] #Turns battleboatP1 into a list
      for line in open('Files/battleboatP1.csv'):
        P1.append(line.split(","))
      P2=[] #Turns battleboatP2 into a list
      for line in open('Files/battleboatP2.csv'):
        P2.append(line.split(","))
      not_done=True
      while not_done:
        system('clear')
        print("Player board:")
        player_board=[]
        for line in open('Files/battleboatP1.csv'): #Called the file to use a string
          player_board.append(line.replace("C","H").replace("D","H").replace("E","H").replace("M"," ").split(",")) #Transform it back into a list but hide boat locations
        display_board(player_board) #Displays the player's board
        print("Hit targets:")
        shot=[]
        for line in open('Files/battleboatP2.csv'): #Called the file to use a string
          shot.append(line.replace("1"," ").replace("2"," ").replace("3"," ").replace("4"," ").replace("5"," ").replace("C","H").replace("D","H").replace("E","H").split(",")) #Transform it back into a list but hide boat locations
        display_board(shot) #Displays player 2 board
        print(CPU_Coordinate)
        P2=sink(P2,"P1") #Player sink
        if open(f"Files/battleboatP2.csv","r").read().find("1")==-1 and open(f"Files/battleboatP2.csv","r").read().find("2")==-1 and open(f"Files/battleboatP2.csv","r").read().find("3")==-1 and open(f"Files/battleboatP2.csv","r").read().find("4")==-1 and open(f"Files/battleboatP2.csv","r").read().find("5")==-1: #Check if P1 has won
          system('clear')
          print("Player board:")
          display_board(P1)
          print("Hit targets:")
          display_board(P2)
          input("Player has won!")
          system('clear')
          not_done=False
        else:
          P1=sink(P1,"P2") #Computer sink
          if open(f"Files/battleboatP1.csv","r").read().find("1")==-1 and open(f"Files/battleboatP1.csv","r").read().find("2")==-1 and open(f"Files/battleboatP1.csv","r").read().find("3")==-1 and open(f"Files/battleboatP1.csv","r").read().find("4")==-1 and open(f"Files/battleboatP1.csv","r").read().find("5")==-1: #Check if P2 has won
            system('clear')
            print("Player board:")
            display_board(P1)
            print("Hit targets:")
            display_board(P2)
            input("Computer has won!")
            system('clear')
            not_done=False
  except:
    a=0