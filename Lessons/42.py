from time import sleep
word = ""
guess = ""
not_done = True
attempts = 0
while not_done and attempts < 5: # While the word is not guessed and 5 attempts haven't happened
  guess=input("Guess the word: ")
  if guess == word: # If the guess is the word
    attempts += 1 
    correct = "CORRECT!" # Makes the final print statement say correct
    not_done = False # Ends the while loop
  else:
    attempts += 1
    correct = "INCORRECT!" # Makes the final print statement say incorrect

print("You were",correct,". Guesses:",attempts)

simon_says = []
adding_instructions = True

while adding_instructions: # Until the user says to stop adding instructions
  instruction = input("Enter a Simon says instruction")
  simon_says.append(instruction) # Adds to a list to save instructions
  answer=input("Would you like to add another? Y/N").upper()
  if answer == "N": # If the user wants to stop
    adding_instructions = False # Stop the while loop

Intros =  ["Simon says...", ""] # Either say simon says or nothing

for x in range(len(simon_says)):
  print(simon_says[x]+simon_says[x]) # Prints something from the intros list then an instruction
  sleep(3)

file=open("Files/spellings.csv","r")
spellings=[]
student_spellings=[]
for item in file:
  spellings.append(item.split(",")) # Adds every item from spellings.csv to a list
file.close()
file=open("Files/spellings.csv","a")
file.write("\n")
print(spellings)
for item in spellings:
  for item in item:
    print(item)
    student_spellings.append(input("Enter the spelling: ").lower())
repeat=0
while repeat<len(student_spellings):
  print(spellings[0][repeat])
  print(student_spellings[repeat])
  file.write(f"{spellings[0][repeat]==student_spellings[repeat]},")
  repeat+=1
file.close()