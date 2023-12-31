from time import sleep
from random import randint, choice
from os import system

print("Numbers:")
a = int(input())
b = int(input())
sum = 0
while b > 0:
  if b % 2 == 1:
    sum = sum + a 
  a = 2*a
  b = b // 2
print(sum)

items=[24,16,35,42,7]
lowest = items[0]
for current in range(1, len(items)):
    if lowest < items[current]:
        lowest = items[current]
print(lowest)


total = 0
for i in range(1,3):
  print(i)
  for j in range(2,5):
    total = total + j
  print(total)

