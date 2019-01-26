"""Intro to Python - Part 1 - Hands-On Exercise."""


import math
import random


# TODO: Write a print statement that displays both the type and value of `pi`
pi = math.pi
print(pi)

# TODO: Write a conditional to print out if `i` is less than or greater than 50
i = random.randint(0, 100)
if i < 50:
    print("Es menor que 50")
if i > 50:
    print("Es mayor que 50")
# TODO: Write a conditional that prints the color of the picked fruit
picked_fruit = random.choice(['orange', 'strawberry', 'banana'])
if picked_fruit == "orange":
    print("Color Naranja")
if picked_fruit == "strawberry":
    print("Color Rojo")
if picked_fruit == "banana":
    print("Color Amarillo")

# TODO: Write a function that multiplies two numbers and returns the result
# Define the function here.
def multiplica(num1, num2):
    resultado = num1 * num2
    return resultado

# TODO: Now call the function a few times to calculate the following answers

print("12 x 96 =", multiplica(12,96))

print("48 x 17 =", multiplica(48,17))

print("196523 x 87323 =",multiplica(196523,87323))
