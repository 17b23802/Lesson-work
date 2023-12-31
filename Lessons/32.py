from random import randint
not_done=True
while not_done:
  password=input("Input a word. You will be asked to input 2 more. The total characters of the three words needs to be greater than 11: ").lower()+input("Input a word. You will be asked to input 1 more: ").lower()+input("Input a word: ").lower()
  if len(password)>11:
    print("The password is",(password.replace("a",chr(randint(33,37))).replace("e",chr(randint(38,42))).replace("i",chr(randint(43,47))).replace("o",chr(randint(58,61))).replace("u",chr(randint(91,94)))[0:len(password)-1]).capitalize()+password.replace("a",chr(randint(33,37))).replace("e",chr(randint(38,42))).replace("i",chr(randint(43,47))).replace("o",chr(randint(58,61))).replace("u",chr(randint(91,94)))[len(password)-1].upper()+input("Make sure your screen is secure before we display the password, then press enter.")[:-9999])
    not_done=False