from time import sleep
from random import randint, choice

sugar_tax = 0.50
print("Sandwich or Wrap?")
bread_type = input().lower()
print("Meat, Vegetarian or Vegan?")
filling_type = input().lower()
print("Cookie, Crisps, Fruit or None")
pudding = input().lower()
print("Fizzy drink, Water, Juice or None")
drink = input().lower()
print("Do you want extra sauce?")
extra_sauce = input().lower()
print("Do you want extra salad?")
extra_salad = input().lower()
if bread_type != "sandwich":
  total_cost = 2.00
else:
  total_cost = 3.00
if extra_sauce == "yes" and extra_salad == "yes":
  total_cost = total_cost + 1.00
else:
  if extra_sauce == "yes":
    total_cost = total_cost + 0.50
  if extra_salad == "yes":
    total_cost = total_cost + 0.30
if filling_type == "vegetarian" or filling_type == "vegan":
  total_cost = total_cost + 1.00
else:
  total_cost = total_cost + 1.50
if pudding == "cookie" and drink == "fizzy drink":
  total_cost = total_cost + sugar_tax
if pudding == "none" or drink == "none":
  total_cost = total_cost - 0.50
print(f"Your total cost is: £{total_cost}")

total_cost = 0.00
crust = input("Would you like a thin or thick crust?")
size = int(input("Pick a pizza size from 8, 10, 12, 14 or 18 inches"))
cheese = input("Would you like cheese? Y/N").lower()
pizza_type = input("Which pizza type would you like? Margherita, Vegetable, Vegan, Hawaiian or Meat Feast?").lower()
code = input("If you have a voucher code, enter it now. Press enter to skip").lower()
if crust == "thin":
  total_cost = total_cost + 10.00
else:
  total_cost = total_cost + 8.00
if size > 10:
  total_cost = total_cost + 2.00
if cheese != "yes":
  total_cost = total_cost - 0.50
if pizza_type == "vegetable" or pizza_type == "vegan":
  total_cost = total_cost + 1.00
if pizza_type == "hawaiian" or pizza_type == "meat feast":
  total_cost = total_cost + 2.00
if code == "FunFriday":
  total_cost = total_cost - 2.00
print("The total cost is",total_cost)