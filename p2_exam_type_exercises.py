#Exercise num.1: Unit Conversion
quantity1 = int(input("Enter the quantity:"))
original_unit = input("Enter the original unit (miles, Farenheit or liters):")
converting_unit = input("Enter the unit you want to convert it to (kilometers, Celsius or gallons):")
def miles():
  kilometers = 0.621371*quantity1
  return kilometers
def Farenheit():
  Celsius = (quantity1 - 32) * 5/9
  return Celsius
def liters():
  gallons = 0.264127 * quantity1
  return gallons
  
if original_unit == "miles":
  kilometers = 0.621371 * quantity1
  print(f"{quantity1} miles is equal to {kilometers} kilometers.")

elif original_unit == "Farenheit":
  Celsius = (quantity1 - 32) * 5/9
  print(f"{quantity1} degrees Farenheit is equal to {Celsius} degrees Celsius.")

elif original_unit == "liters":
  gallons = 0.264127 * quantity1
  print(f"{quantity1} liters is equal to {gallons} gallons.")

#Exercise num.2: Road Trip Planning
distance = float(input("Enter the distance in miles:"))
mpg = float(input("Enter the car's miles per gallon:"))
price_gasoline = float(input("Enter the current price of gasoline per gallon:"))
days = int(input("Enter the number of days you plan to travel:"))

def total_price():
  total_price = (distance/mpg)* price_gasoline * days
  print(f"The total price of the trip is ${total_price}")

total_price()

#Exercise num.3: Multiple Discount Purchase
original_price = float(input("Enter the price of the product:"))
category = input("Enter the category (A, B or C):")
num_products = int(input("Enter the number of products purchased:"))
if category == "A":
  print(f"Price before discount: {original_price}")
  print("Discount applied: 10%")
  final_price = original_price - (original_price*.10)
  print(f"Price after discount {final_price}")
  if num_products > 10:
    print("Additional discount applied (more than 10 products): 5%")
    final_price_additional = original_price - (original_price*.10) - (original_price*.05)
    print(f"Price after additional discount {final_price_additional}")

elif category == "B":
  print(f"Price before discount: {original_price}")
  print("Discount applied: 5%")
  final_price = original_price - (original_price*.05)
  print(f"Price after discount {final_price}")
  if num_products > 10:
    print("Additional discount applied (more than 10 products): 5%")
    final_price_additional = original_price - (original_price*.05) - (original_price*.05)
    print(f"Price after additional discount {final_price_additional}")

elif category == "C":
  print(f"Price before discount: {original_price}")
  print("Discount applied: 2%")
  final_price = original_price - (original_price*.02)
  print(f"Price after discount {final_price}")
  if num_products > 10:
    print("Additional discount applied (more than 10 products): 5%")
    final_price_additional = original_price - (original_price*.02) - (original_price*.05)
    print(f"Price after additional discount {final_price_additional}")

import random
#Exercise num.4: Role-Playing Game (RPG) Simulation
print("Welcome to the Simple RPG Game!")
print("Choose your character: 1.Police 2.Citizen 3.Military")
character = input("Enter the number of your chosen character:")
print("You have encountered an armed person. Roll a 20-sided dice to determine your success.")

if character == "1":
  print("Rolling the dice...")
  number = int(random.randint(0,20))
  print(f"You rolled {number}")
  if number <= 15:
    print("Oopsies, you couldn't defeat the armed person :(, try again.")
  if number > 15:
    print("Congratulations! You succesfully defeated the armed person.")

if character == "2":
  print("Rolling the dice...")
  number = int(random.randint(0,20))
  print(f"You rolled {number}")
  if number < 20:
    print("Oopsies, you couldn't defeat the armed person :(, try again.")
  if number == 20:
    print("Congratulations! You succesfully defeated the armed person.")

if character == "3":
  print("Rolling the dice...")
  number = int(random.randint(0,20))
  print(f"You rolled {number}")
  if number <= 3:
    print("Oopsies, you couldn't defeat the armed person :(, try again.")
  if number > 3:
    print("Congratulations! You succesfully defeated the armed person.")
