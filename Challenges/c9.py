from time import sleep
from termcolor import colored
from random import shuffle
from os import system
def A(questions,asked,correct,not_done):
  file=open("Questions.txt","r")
  for line in file:
      line = line.rstrip()
      questions.append(line)
  while not_done:
    print(colored("To end, type",'cyan'),colored("end.",'red'),colored(" Press enter when you have finished writing the answer and the answer key will appear. When you have finished looking at the answer key, press enter again.",'cyan'))
    shuffle(questions)
    q=questions[0].split(",")
    answer=input(colored(q[0],'yellow')).lower()
    if answer=="end":
      print(colored("You must be done now, your answers will be uploaded. You got a total of",correct,"questions right out of",asked,"so have an accuracy of",correct/asked*100,"%",'green'))
      not_done=False
    else:
      print(q[1])
      q=input()
      system('clear')