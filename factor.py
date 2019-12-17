def factor(n):# Defining factor and taking input
    fact = []
    if n == 0:# Evaluating whether input is 0 or 1
        return 0
    elif n == 1:
        return 1
    elif n%2 != 0:# Evaluating if number is odd
        for i in range(1,int((n-1)/2)):# If it is setting a range for possible factors
            if n%i == 0:# Evaluating every single number whether divisible? (included in range)
                fact.append(i)# If it is adding it in a list
        print(fact,n)# Returning the final output
    elif n%2 == 0:# If it is not even ,it has to be odd
        # Doing the same process what we did for odd numbers
        for i in range(1,int(n/2)+1):
            if n%i == 0:
                fact.append(i)
        print(fact,n)        
                    
               
        
 
