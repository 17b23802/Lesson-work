from time import sleep
from random import randint, choice
from os import system

def A():
  file = open("Stats.txt","w")
  not_done=True
  while not_done:
    try:
      maxEVS = int(input("What do you want the max evs to be?"))
      not_done=False
    except ValueError:
      print("Must be a number")
  ATKEV = randint(0,maxEVS)
  DEFEV = randint(0,maxEVS)
  SPATKEV = randint(0,maxEVS)
  SPDEFEV = randint(0,maxEVS)
  HPEV = randint(0,maxEVS)
  SPDEV = randint(0,maxEVS)
  ATKIV = randint(0,31)
  DEFIV = randint(0,31)
  SPATKIV = randint(0,31)
  SPDEFIV = randint(0,31)
  HPIV = randint(0,31)
  SPDIV = randint(0,31)
  Nature = randint(1,25)
  if Nature == 1:
    Nature = "Timid"
  elif Nature == 2:
    Nature = "Bashful"
  elif Nature == 3:
    Nature = "Rash"
  elif Nature == 4:
    Nature = "Shy"
  elif Nature == 5:
    Nature = "Adamant"
  elif Nature == 6:
    Nature = "Bold"
  elif Nature == 7:
    Nature = "Hardy"
  elif Nature == 8:
    Nature = "Careful"
  elif Nature == 9:
    Nature = "Lonely"
  elif Nature == 10:
    Nature = "Brave"
  elif Nature == 11:
    Nature = "Naughty"
  elif Nature == 12:
    Nature = "Docile"
  elif Nature == 13:
    Nature = "Impish"
  elif Nature == 14:
    Nature = "Lax"
  elif Nature == 15:
    Nature = "Hasty"
  elif Nature == 16:
    Nature = "Serious"
  elif Nature == 17:
    Nature = "Jolly"
  elif Nature == 18:
    Nature = "Naive"
  elif Nature == 19:
    Nature = "Modest"
  elif Nature == 20:
    Nature = "Mild"
  elif Nature == 21:
    Nature = "Quiet"
  elif Nature == 22:
    Nature = "Calm"
  elif Nature == 23:
    Nature = "Gentle"
  elif Nature == 24:
    Nature = "Sassy"
  elif Nature == 25:
    Nature = "Quirky"
  Gender = randint(0,1)
  if Gender == 0:
    Gender = "Male"
  else:
    Gender = "Female"
  file.write(f"Gender = {Gender}"+'\n'+f"Nature = {Nature}"+'\n'+f"Attack IV = {ATKIV}"+'\n'+f"Defense IV = {DEFIV}"+'\n'+f"Special Attack IV = {SPATKIV}"+'\n'+f"Special Defence IV = {SPDEFIV}"+'\n'+f"Speed IV = {SPDIV}"+'\n'+f"HP IV = {HPIV}"+'\n'+f"Attack EV = {ATKEV}"+'\n'+f"Defense EV = {DEFEV}"+'\n'+f"Special Attack EV = {SPATKEV}"+'\n'+f"Special Defence EV = {SPDEFEV}"+'\n'+f"Speed EV = {SPDEV}"+'\n'+f"HP EV = {HPEV}")
  file.close()
  file = open("Stats.txt","r+")
  for line in file:
    print(line)