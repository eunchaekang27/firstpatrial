def grade():
  print("Hi, I'm a program that calculates an average of your grades.")
  print("Write your first grade")
  a=input()
  print("Write your second grade")
  b=input()
  print("Write your third grade")
  c=input()
  result=(float(a)+float(b)+float(c))/3
  print("Your grade average is", result)
  if result<70 : print("You failed :(")
  if result>70 : print("You passed :D")

grade()

def currency():
  print("Hi, I'm a code that turns your dollars into euros")
  print("Insert your amount in dollars")
  a=input()
  result=float(a)*(0.93)
  print("Your amount in euros is", result)

currency()

def bmi():
  print("Hi! I am a machine that caculates your Body Mass Index (BMI)" )
  print("First, you need to put your weight in kilograms, and then you need to put height in meters.")
  print("Put your weight")
  w=input()
  print("Put your height")
  h=input()
  print("Calculating your BMI")
  result=float(w)/((float(h))**2)
  print("Your BMI is", result)
  if result<18.5 : print("You're underweight")
  if 18.5<result<24.9 : print("You're normal")
  if 24.9<result<29.9 : print("You're overweight")
  if 29.9<result<34.9 : print("You're obese")
  if result>35 : print("You're extremely obese")

bmi ()

