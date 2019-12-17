# test
q1 = input("what is 1/4 of 1/5 ? ")
q1a = '1/20'
score = 0

if q1 == q1a:
    print("yah! good start")
    score = score + 1
else:
    print("oh!that's incorrect")


q2 = input("what is 20% of 50 ? ")
q2a = '10'
if q2 == q2a:
    print("that is correct")
    score = score + 1
else:
    print("oh! that's incorrect")

    
q3 = input("what is 25% of 52 ? ")
q3a = '13'
if q3 == q3a:
    print("that is correct")
    score = score + 1
else :
    print("that is incorrect")

q4 = input("what is X if x = 2 + 4*4 ? ")
q4a = '18'
if q4 == q4a:
    print("that is correct! ")
    score = score + 1
else:
    print("oh ! that is incorrect")
    
q5 = input("what is x in x + 3*6/9 = 8 ? ")
q5a = '6'
if q5 == q5a:
    print("great ! you ended well")
    score = score + 1
else :
    print("oh! you got that wrong")
    

print("your final score is",score," out of 5 questions")
if score == 0 or score == 1 :
    print(" you got to improve")
    print("just start practising for everyday")
elif score == 2 or score == 3:
    print(" though you did well you can still improve")
elif score == 4:
    print(" you did very well ,just one mistake which could have been avoided")
else:
    print("you did amazing, keep it up!")
