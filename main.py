from time import sleep
from termcolor import colored
from random import randint, choice
from os import system

challenge = input(colored("What lesson number? ",'cyan')).lower().strip().replace(" ","")
system('clear')
try:
  exec(open(f"Lessons/{challenge}.py","r").read())
except:
  try:
    exec(open(f"Challenges/{challenge}.py","r").read())
  except:
    #try:
      exec(open(f"Revision/{challenge}.py","r").read())
    #except:
    #  fun= ["gottem","jojo","lastsurprise","lifewillchange","rick","sans"]
    #  exec(open(f"Fun/{choice(fun)}.py","r").read())