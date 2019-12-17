def amic(amic_fac):
    sum_fac = {}
    amicable = {}
    for i in range(amic_fac, 0, -1):
        if len(factor(i)) == 0:
            sum_fac[i] = 0
        else:
            fac = (add_lst(factor(i)))
            if sum_fac.get(fac, -1) == i:
                amicable[i] = fac
            sum_fac[i] = fac
    return amicable
        
        
def factor(fact):
    fac_lst = []
    for i in range(1,int(fact/2)+1):
        if fact%i == 0:
            fac_lst.append(i)
    return fac_lst

def add_lst(add):
    res = add[0]
    if len(add) == 0:
        return 0
    for i in range(1,len(add)):
        res = res + add[i]
    return res
