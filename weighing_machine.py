#!/usr/bin/python3
# ideal weight
name = input("what is your name ? ")
height = eval(input("what is your height ? "))
weight = eval(input("what is your weight ? "))

ideal_weight = height - 100
# tolerance for ideal weight
tolerance = 2 / 100
# ideal weight upper lower limit
lower_ideal = ideal_weight - ideal_weight * tolerance
upper_ideal = ideal_weight + ideal_weight * tolerance

# Tolerance for obesity/malnutrition
high_tolerance = 10 / 100
lower_tolerance = ideal_weight - ideal_weight * high_tolerance
upper_tolerance = ideal_weight + ideal_weight * high_tolerance

malnourished = weight < lower_tolerance
obese = weight > upper_tolerance

underweight = weight < lower_ideal and weight < lower_tolerance
overweight = upper_ideal < weight < upper_tolerance

right_weight = lower_tolerance < weight < upper_tolerance

if underweight:
    print(name, "you are a bit thin for your height")

elif malnourished:
    print(name, "you are too thin for your height")
    print("you need to start eating nicely")

elif overweight:
    print(name, "you need to reduce your food intake a bit")

elif obese:
    print(name, "you are too fat for your height")
    print("you really need to diet to stay healthy")

else:
    print(name, "you are a very healthy person")
    print("keep it up")
