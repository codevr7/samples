#divisibility
n = eval(input("pick a number"))
if n%5 == 0 and n%3 != 0:
    print("fizz")
elif n%3 == 0 and n%5 != 0:
    print("buzz")
elif n%5 == 0 and n%3 == 0:
    print("fizzbuzz")
else:
    print(n)
