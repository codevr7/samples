import random
the_number = random.randint(1,10)
guess = int(input("guess a number between 1 to 10"))
if guess > the_number:
    print("guess was too high,try again")
if guess < the_number:
    print("guess was too low,try again")
if guess == the_number:
    print("yeh that was right,good one")
