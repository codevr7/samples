# A function for sorting only odd numbers from a list of mixed numbers
def odd_sort(n):
    l = len(n)# The length of the input
    for i in range(0, l):# A range for 0 to length of input
        for j in range(i, l):# A second range for evaluating for each number
            if n[i]%2 != 0:# Evaluating each number, whether odd or not
                if n[j]%2 != 0:# Eval       
                    if n[i] > n[j]:
                        n[i], n[j] = n[j], n[i]
                        
    return n            
        
        
 
