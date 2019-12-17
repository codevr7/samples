# LCM
def lcm(n,m):# Defining a function for LCM and its inputs
    inp_1 = []# 2 empty lists
    inp_2 = []
    if n < m:
        larger = m
        small = n
    else:
        larger = n
        small = m
    for i in range(1,11):
        val = larger*i
        val_1 = small*i
        inp_1.append(val_1)
        inp_2.append(val)    
    return inp_1,inp_2
 
