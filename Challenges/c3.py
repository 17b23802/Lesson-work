from time import sleep
from random import randint, choice

def A():
  email=input("Please enter an email address for validation:")
  if -1 != email.find(" "):
    print("You can't have spaces in an email address")
  elif -1 == email.find("@"):
    print("You have to have an @ in an email address")
  elif email.find("@") > email.find("."):
    print("You have to have a . in an email address after an @")
  elif email.find("@")  > 64:
    print("Email addresses have to be under 64 characters before the @")
  elif email.find(".") - email.find("@") < 253:
    print("The domain name is too long")
  else:
    print("VALID!")
