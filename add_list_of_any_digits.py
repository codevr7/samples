# A function for addtion in lists
def add_list(n1, n2):
    length_1 = (len(n1))
    carry = 0
    final = []
    for i in range(length_1-1,-1,-1):
        s = n1[i] + n2[i] + carry
        if s > 9:
            carry = 1
        else:
            carry = 0
        final.insert(0, s%10)
    if carry > 0:
        final.insert(0, carry)
    return final
            
        
        
        
        
        
        

    
