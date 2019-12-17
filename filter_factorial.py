# Function for filtering factorials from given list
def check_fact(n):
    fact = 1# Initial number
    add = 2
    check = False
    final = []
    
    while not check:# Loop until number found
        fact = fact*add# Repeat process
        add += 1
        if fact >= n:# If factorial equal to or exceeds number
            check == True # Exit the loop
            if fact == n:# Number is equal to factorial
                return True
            else:
                return False
                
def filter_fact(lst):
    ret_lst = []
    for elt in lst:
        if check_fact(elt) == True:
            ret_lst.append(elt)
    return ret_lst        
            

