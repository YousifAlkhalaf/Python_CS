import math

w = 5
x = 4
y = 8
z = 2

print("w + x / y")
print("Prediction: 5.5")
result = w + x / y
print("Result:", result)

print("\ny // x + x % y")
print("Prediction: 6")
result = y // x + x % y
print("Result:", result)

print("\nmath.sqrt(x) + y")
print("Prediction: 10")
result = math.sqrt(x) + y
print("Result:", result)

print("\nw ** z")
print("Prediction: 25")
result = w ** z
print("Result:", result)

print("\nresult += 5")
print("Prediction: 30")
result += 5
print("Result:", result)