def mine(n): # defining the series MINE
    if n == 1: #if n input is 1 or 2 giving the respective outputs
        return 0
    elif n == 2:
        return 1
    else: #if n input is not 1 or 2...
        x = 1
        y = 1
        for i in range (1,n-1): #setting a range for number            
            z = x + (y+1) #how this series works
            y = y + 1 #changing the values
            x = z
        return z #returning the output   
            
