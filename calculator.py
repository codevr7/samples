#calculator
operations = input("pick an arithmetic operation.(a/s/m/d)")
number_1 = input("select a number you want to calculate(1,9)")
number_2 = input("select another number you want to pick(1,9)")
if operations == 'a':
    print(input("the answer to the problem is ", eval(number_1 + number_2)))
if operations == 's':
    number_1 - number_2
if operations == 'm':
    number_1 * number_2
if operations == 'd':
    number_1 / number_2
    


            
