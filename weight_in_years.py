import sys
print("please enter your current weight")
weight = int(sys.stdin.readline())
print("type in your potential increse per year")
potin = int(sys.stdin.readline())
print("for how many years do you want to calculate")
years = int(sys.stdin.readline())
finweight = weight + potin * years
print("your weight in ",years,"years is going to be ",finweight)
