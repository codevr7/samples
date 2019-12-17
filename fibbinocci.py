def fib(n):  # defining fibbinocci series
    if n == 1: # evaluating if number is 1 or 2
        return 1# Output for 1st fibbinocci number
    elif n == 2:
        return 1# The output if input == 2
    else: # if it is not 
        value_1 = 1 # giving the first and second number in fib series a variable
        value_2 = 1
        for i in range (1,n-1): #a loop for 1 to the number -1
            value = value_1 + value_2 #how the the fibbinocci series works
            value_1 = value_2 # changing the values depending on the number and the range
            value_2 = value
        return value # Returning the final output 
            
        
   
