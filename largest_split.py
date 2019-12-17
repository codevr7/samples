# A function for finding largest possible product of sums of input
def split(num):
    if num < 4:
        return num
    largest = num - 1 # Initial largest
    split_lst = reduce(num)# Finding all pairs of sums, saving it in a list
    for i in range(len(split_lst)):# Iterating through entire list
        # Evaluating if product of list is greater than largest
        if prod(split_lst[i]) > largest:
            largest = prod(split_lst[i])
    return largest
        
# A function for reducing a number systematically
def reduce(inp):
    search = False
    inp = [inp]
    inp_lst = sum_pair(inp)
    ret = []
    while not search:
        check = []
        ret.extend(inp_lst)
        for i in range(len(inp_lst)):
            if (inp_lst[i])[0] > 4:
                check.append((inp_lst[i]))
            
        if len(check) == 0:
            search == True
            break
        inp_lst = []
        for j in range(len(check)):
            inp_lst.extend(sum_pair(check[j]))

    return ret

# A function for finding product of all elements present in list 
def prod(lst):
    mult = lst[0]
    for i in range(1, len(lst)):
        mult *= lst[i]
    return mult

# A function for reducing a given number to it's sum pairs
def sum_pair(val_lst):
    lst = val_lst.pop(0)# Variable for 1st element of input
    ret = []
    for i in range(int(lst/2), 1, -1):
        proc = []
        proc.append([lst - i, lst - (lst - i)])
        (proc[0]).extend(val_lst)        
        ret.append((proc[0]))
    return ret
