#Replit link: https://replit.com/join/rqrxrjjgpe-eun-chaechae
print("Hi! I'm a program that takes care of Ruby, a very special plant :)")

#Care criteria:

#Temperature:
environment_temp = float(input("Insert the current temperature in degrees Celsius:"))
if 20 <= environment_temp <= 25:
  print("Good conditions")

elif environment_temp < 20:
  print("Bring it inside the house")

elif environment_temp > 25:
  print("Bring it inside the house and turn on the fan")

#Watering:
day = str(input("Insert the current day of the week:"))
if day == "Tuesday" or day == "Thursday" or day == "Saturday":
  print("Water Ruby")

#Humidity percentage:
environment_h = float(input("Insert the percentage of humidity in the air around Ruby:"))
if environment_h < 20:
  print("You should water Ruby")

elif 20 <= environment_h <= 22:
  print("Suitable humidity")

elif environment_h > 22 and day == "Monday" or day == "Wednesday" or day == "Friday" or day == "Sunday":
  print("It is not necessary to water Ruby.")
