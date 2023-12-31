def A():
  file=open("Words.txt","r")
  checklist = []
  for line in file:
      line = line.rstrip()
      checklist = line.split(" ")
  print(f"There are {len(checklist)} words in the file.")