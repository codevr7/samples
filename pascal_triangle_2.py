# A function for finding Pascal's Triangle
def pascal(line):
    init = [0,1,0]
    final = [[0,1,0]]
    for i in range(line-1):
        init = add_lst(init)
        final.append(init)
    return final

# A function for finding sum of consecutive elements in list ,for whole list
def add_lst(lst):
    if len(lst) == 0:
        return 0
    
    ret = []# Empty list
    for i in range(0,len(lst)-1):# Range for computing entire list
        ret.append(lst[i] + lst[i+1])# Summing up consecutive elements
    ret.append(0)
    ret.insert(0, 0)
    return ret
