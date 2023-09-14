def temperature():
  print("Hi! I'm a program that can convert degrees Celsius into Farenheit and Kelvin :D")
  print("First, write the temperature in Celsius")
  a=input()
  result=float(a)*9/5+32
  print("Your temperature in Farenheit is", result)
  result=float(a)+273.15
  print("Your temperature in Kelvin is", result)

temperature()

def area():
  print("Input the length")
  l=input()
  print("Input the width")
  w=input()
  result=(float(l)*2)+(float(w)*2)
  print("The perimeter is", result)
  result=float(l)*float(w)
  print("The area is", result)

area()

def fuel():
  print("Input the distance traveled in kilometers")
  a=input()
  print("Input the amount of fuel consumed in liters")
  b=input()
  result=float(a)/float(b)
  consumption=float(result)*2.35215
  print("The consumption in km/l is", result)
  print("The consumption in mi/gal is", consumption)

fuel()

def discount():
  print("Input the original price")
  a=input()
  print("Input the discount percentage")
  b=input()
  result=float(a)-(float(a)*(float(b)/100))
  print("Your final price is", result)
  result=float(a)*(float(b)/100)
  print("The discount amount is", result)
  print("The percentage of discount applied is", b)

discount()

def interest():
  print("Enter the invested amount")
  a=input()
  print("Enter the annual interest rate")
  b=input()
  print("Enter the number of years")
  c=input()
  result=float(a)*float(b)*float(c)
  print("The amount of interest you earned is", result)
  result=(float(a)*float(b)*float(c))+float(a)
  print("The total amount after the investment is", result)

interest()

def fastfood():
  print("Input the original price of the food")
  a=input()
  print("Input the percentage of the discount coupon")
  b=input()
  result=float(a)-(float(a)*(float(b)/100))
  print("The final price is", result)
  result=float(a)*(float(b)/100)
  print("The money saved is equal to", result)

fastfood()
