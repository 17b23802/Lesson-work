from time import sleep
from random import randint, choice

not_validated = True
while not_validated:
  try:
    print("Enter a number between 1 and 10:")
    number = int(input())
    if number >= 1 and number <= 10:
      not_validated = False
    else:
      print("Number entered out of range")
  except ValueError:
    print("You must enter a number:")
print("F R I E N D  2 : electric boogaloo")

name = ""
not_validated = True
print("Enter a name:")
while not_validated:
    name = input()
    if name.strip() == "":
      print("Name cannot be left blank")
    else:
      not_validated = False
print(f"Stored name: {name}")

print("""Welcome to the times table quiz. 
Enter a times table that you would like to be tested on:""")
score = 0
y = 0
while y == 0:
  try:
    times_table = int(input())
    y = 1
  except ValueError:
    print("You must enter a number")
print("Enter the maximum value for your times table:")
while y == 1:
  try:
    max_value = int(input())
    y = 2
  except ValueError:
    print("You must enter a number")
max_value = max_value+1
answer = 0
print(f"Here is your quiz on the {times_table} times table")
for x in range(1,max_value):
    answer = x * times_table
    print(f"{x} times {times_table} is ...")
    while y == 2:
      try:
        user_answer=int(input("Answer: "))
        y = 3
      except:
        print("It has to be a number")
    if user_answer == answer:
      print("Correct")
      score = score + 1
    else:
      print("Incorrect")
    y = 2
if score == max_value-1:
  print(f"Amazing, you scored a perfect {score}")
elif score >= max_value/2 and score != 0:
  print(f"Not bad, you scored {score} out of {max_value-1}. Try a bit harder for that perfect score")
elif score != 0:
  print(f"You scored {score} out of {max_value}. Learn basic maths")
else:
  print("You're a faliure")