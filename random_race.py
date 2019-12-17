import random
import turtle 
p1 = input("type in your user name")
p2 = input("type in second player's name")
print(" the colors are red for",p1," and blue for ",p2)
p1 = turtle.Pen()
p1 = turtle.pencolor("red")
p2 = turtle.Pen()
p2 = turtle.pencolor("blue")
print("the first chance goes to ",p1)
p1.forward(random.randint(1,10))



    
