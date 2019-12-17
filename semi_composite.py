# Defining a function for finding semi-prime
def semiprime(num):
    lst_prime = []
    if prime(num) == True:# Checking if input is prime
        return False# If it is returning FALSE, semiprime should be composite
    
    fact = factor(num)# Saving factors of input in a variable  
    # Process for adding prime factors of input to seperate list
    for i in range(len(fact)):
        if prime(fact[i]) == True:
            lst_prime.append(fact[i])
            
    # Range for multiplying each pair of prime-factor
    for j in range(len(lst_prime)):
        for k in range(j, len(lst_prime)):
            if j == k:# If j is same as k and ...
                if fact[j]*fact[k] == num:# when multiplied it gives input
                    print("Semiprime")# Square semi-prime
                    return True             
            if fact[j]*fact[k] == num:# If j not equal to k,and product = input
                print("Square-Free semiprime")# Square-Free semi-prime
                return True       
    # If loop exited without result
    return False



# Defining function for finding if prime or non-prime
def prime(comp):
    for i in range(2,comp):
        if comp%i == 0:
            return False
    return True



# Defining function for finding factors
def factor(f):
    ret = []
    for i in range(2,f):
        if f%i == 0:
            ret.append(i)
    return ret
