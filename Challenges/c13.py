text = input("Enter the string you want to count the vowels in: ")
a_count=0
e_count=0
i_count=0
o_count=0
u_count=0
for letter in text:
  if letter == "a":
    a_count=a_count+1
  if letter == "e":
    e_count=e_count+1
  if letter == "i":
    i_count=i_count+1
  if letter == "o":
    o_count=o_count+1
  if letter == "u":
    u_count=u_count+1
print(f"There are {a_count+e_count+i_count+o_count+u_count} vowels in the string. There are {a_count} a's, {e_count} e's, {i_count} i's, {o_count} o's and {u_count} u's")
    