import random
number = random.randint(1,10)
guess = int(input("type a number,any number ? "))
while guess != number:    
    if guess > number :
            print("your guess was high,please try again")
    if guess < number :
            print("your guess was low ,please try again")
    guess = int(input("guess again"))
print("yesss,you got it right")                
