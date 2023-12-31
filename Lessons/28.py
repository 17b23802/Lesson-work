def num_dogs():
  return int(input("How many dogs have you walked?"))

def num_days():
  return int(input("How many days have you walked the dogs for?"))

def num_walks(total_dogs, total_days):
  return total_dogs*total_days

def total_charge(total_walks):
  return total_walks*4

def invoice(total_dogs, total_days, total_walks, total_cost):
  print(f"You walked {total_dogs} dogs for {total_days} days so you paid for {total_walks} walks and so will be charged {total_cost}")

total_dogs = num_dogs()
total_days = num_days()
total_walks = num_walks(total_dogs,total_days)
total_cost = total_charge(total_walks)
invoice(total_dogs, total_days, total_walks, total_cost)
