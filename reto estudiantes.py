https://replit.com/join/kdkhjjqgtv-eun-chaechae

print("Hi, I'm a program that evaluates students")
av_grade = int(input("Input your average grade from 0-100"))
c_participation = input("Is your classroom participation good? (Answer with yes or no)")
p_score = int(input("Insert your project score from 0-100"))

if av_grade >= 75 and c_participation == "yes":
  print("You are in a good academic standing.")

if p_score > 90:
  print("You received a distinction.")

if av_grade < 60 or c_participation == "no":
  print("You need to improve your performance")
