# Factorial Programme
n = int(input("Enter in the number you want to find factorial of: "))
fact = 1
if n == 0:
    print("the factorial of 0 is 1")
if n < 0:
    print("can not find factorial of negative numbers")

else:
    for i in range(2, n + 1):
        fact = fact * i

    print("the factorial of", n, "is", fact)
