# Defining a function for finding prime-factors of a number
def prime_fact(n):
    final = []
    comp = []# An empty list
    prime_found = False
    # Checking if input is prime
    if prime(n) == True:# If it is ...
        final.append(1)# Cannot be further factorized hence returning input
        final.append(n)
        return final
    
    factors = pair_fact(n)
    while not prime_found:# Until factor list entirely prime
        for i in range(len(factors)):
            if prime(factors[i]) == False:# If composite number in factor 
                comp.append(factors[i])# Add composite number in list
            else:
                final.append(factors[i])
        if len(comp) == 0:# If no composite factor in list
            return final 
            prime_found == True # Exit while loop
        # Else
        comp = comp[0]
        factors = pair_fact(comp)#Find pair factor of composite number
        comp = []# Composite list length, back to zero
     
# Defining a function for finding a pair of factors
def pair_fact(fact):
    for i in range(int(fact/2),1,-1):# Range for processing factors
        if fact%i == 0:
            pair_1 = i# First factor found ,hence stop process
            pair_2 = int(fact/i)# Finding factor pair of first factor
            return pair_1,pair_2# Returning pair of factors

# Defining a function for evaluating if PRIME
def prime(check):
    for i in range(2,int(check/2)):
        if check%i == 0:
            return False
    return True
