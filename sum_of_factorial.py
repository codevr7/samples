# Defining a function for finding sum of digits of factorial
def sum_fact(add):
    fac = factorial(add)# Finding factorial of input
    fac = list(map(int, str(fac)))# Breaking-down factorial into a list
    fac = add_lst(fac)# Adding broken down list ,finding sum of digits
    return fac

# Defining a function for finding factorial of a given number
def factorial(fact):
    mult = fact
    for i in range(fact-1,1,-1):
        mult = mult*i
    return mult

# Defining a function for adding a list
def add_lst(lst_add):
    add = lst_add[0]# Initial
    for i in range(1,len(lst_add)):# Range for length of input list
        add = add + lst_add[i]# Adding next element , saving to variable
    return add
