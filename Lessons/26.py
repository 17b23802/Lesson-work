def change_colour(colour):
  print(f"Your current colour is {colour}")
  print("What would you like to change it to?")
  return input()

colour = "Red"
colour = change_colour(colour)
print(f"Your current colour is {colour}")