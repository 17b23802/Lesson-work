from time import sleep
from termcolor import colored
from random import randint
from os import system

numbers = [1,1,2,3,5,8,13,21,34,55,89,"No"]

str_numbers = []
for number in numbers:
  str_numbers.append(str(number))

data = ",".join(str_numbers)
file = open("Files/fibinacci.csv", "w")
file.write(data)
file.close()

times=int(input("Enter the times table you would like:"))
numbers=[1,2,3,4,5,6,7,8,9,10,11,12]
str_numbers=[]
for number in numbers:
  number=number*times
  str_numbers.append(str(number))
data = ",".join(str_numbers)
file = open("Files/times.csv", "w")
file.write(data)
file.close()


number_grid = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
grid=[]

x=0
while x<10:
  x=x+1
  y=[]
  for number in number_grid:
    y.append(str(number+((x-1)*10)))
  grid.append(y)
data=""
for item in grid:
  for item in item:
    data=data+item+","
  data=data+"\n"
file = open("Files/grid.csv", "w")
file.write(data)
file.close()

data=""
for item in grid:
  for item in item:
    if int(item)%2 == 0 and int(item)%5 == 0:
      data=data+"FizzBuzz,"
    elif int(item)%2 == 0:
      data=data+"Fizz,"
    elif int(item)%5 == 0:
      data=data+"Buzz,"
    else:
      data=data+item+","
  data=data+"\n"
file = open("Files/FizzBuzz.csv", "w")
file.write(data)
file.close()
