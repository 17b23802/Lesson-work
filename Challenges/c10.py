def A():
  word = input("Enter a word to check if it is a palndrome(is spelt the same backwards and forwards):")
  i = 0
  valid_palindrome = True
  while valid_palindrome and i<len(word):
    if word[i] != word[len(word)-1-i]:
      valid_palindrome = False
    else:
      i = i+1
      
  if valid_palindrome:
    print(f"{word} is a palindrome.")
  else:
    print(f"{word} is not a palindrome.")