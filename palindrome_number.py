# Defining a funcion for finding largest palindrome below input
def largest_palin(inp):
    lower = [1]
    upper = []
    for i in range(inp-1):
        lower.insert(len(lower),0)
    for j in range(inp):
        upper.append(9)
    upper = int("".join(map(str, upper)))
    lower = int("".join(map(str, lower)))
    maxi = lower**2
    for k in range(maxi,0,-1):
        if is_palin(k) == True:
            if prime(k) == False:
                for x in range(len(factor(k))):  
                    if x <= upper and x >= lower:
                        print(k)
                        print(k/x)
                        return x
                    
# Defining a function for finding if palindrome 
def is_palin(palin):
    lst_palin = list(map(int, str(palin)))# Converting integer value to list
    inp_con = []
    l = len(lst_palin)
    
    # Process for making input upside down
    for i in range(0,l):
        inp_con.insert(0,lst_palin[i])
        
    # If opposite input is same as input
    if inp_con == lst_palin:
        return True # Palindrome is true
    # Else
    else:
        return False # False
  
def factor(fact):
    fact_lst = []
    for i in range(2,int(fact/2)):
        if fact%i == 0:
            fact_lst.append(i)
    return fact_lst

# Defining a function for checking if prime
def prime(check):
    for i in range(int(check/2),1,-1):
        if check%i == 0:
            return False
    return True
