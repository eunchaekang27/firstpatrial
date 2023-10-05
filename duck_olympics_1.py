def suma(a,b):
  x = a + b
  return x

def resta(a,b):
  x = a - b
  return x

print("Dame el primer número:")
a = int(input())
print("Dame el segundo número:")
b = int(input())
print("La suma da",suma(a,b), "y la resta da", resta(a,b))


def multiplication(a,b):
  x = a * b
  return x

def division(a,b):
  x = a/b
  return x

print("Give me the first number:")
a = int(input())
print("Give me the second number:")
b = int(input())
print("The multiplication gives you", multiplication(a,b), "and the division gives you", division(a,b))

def conversion(km,m):
  m = km*1000
  return m

print("Give me the number of kilometers that have passed:")
km = int(input())
m = km*1000
print(conversion(km,m), "meters have passed")


def triangle_area(b,h):
  a = (b*h)/2
  return a

print("Give me the base of the triangle:")
b = int(input())
print("Give me the height of the triangle:")
h = int(input())
print("The area of the triangle is", triangle_area(b,h))
