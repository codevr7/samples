def hcf(n1,n2):
    fac_n1 = []
    fac_n2 = []
    
    for k in range(n1,0,-1):
        if n1%k == 0:
            fac_n1.append(k)
            
    for i in range(n2,0,-1):
        if n2%i == 0:
            fac_n2.append(i)
    
    for i in range(len(fac_n1) - 1 ,-1,-1): 
        if not fac_n1[i] in fac_n2: 
            del fac_n1[i]
            
    return fac_n1[0]
          
            
            
            

