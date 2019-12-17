# Function for finding breakpoint
def breakpoint(n):
    n = list(map(int,str(n)))# Converting INT input to LIST
    length = len(n)
    lst_1 = []
    lst_2 = []
    lst_1.append(n[0])# 1st list which holds first item of list
    
    for k in range(1,len(n)):
        lst_2.append(n[k])# Adding rest to other list
        
    for i in range(length-1):
        if add(lst_1) == add(lst_2):# If sum of 1st list equals to 2nd list
            return True
        #If not check again
        lst_1.append(lst_2[0])
        del lst_2[0]
        
    #If loop exited
    return False

#Function for adding list    
def add(lst):
    l = len(lst)
    init = 0
    sum_up = lst[0]

    #For the length of list add
    for i in range(l-1):
        sum_up = sum_up + lst[init+1]
        init += 1
    return sum_up
    
