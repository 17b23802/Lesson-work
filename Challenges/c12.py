def A():
  word=input("Input a word to turn into Pig Latin: ")
  final_word=word[1:]
  if word[0] == "a" or word[0] == "e" or word[0] == "i" or word[0] == "o" or word[0] == "u":
    final_word = word + "ay"
  else:
    final_word = final_word + word[0] + "ay"
  print(f"{word} is {final_word} in Pig Latin.")