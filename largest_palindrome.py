def largest_pal(digits):
    upper = largest_digits(digits)# Biggest possible number
    largest = 1

    for i in range(upper, 0, -1):
        for j in range(i, 0, -1):
            res =  i * j
            if res < largest:
                break
            if is_pal(res) == True:
                largest = res
                break
    return largest
                
def is_pal(pal):
    pal = list(map(int, str(pal)))
    check = []
    l = len(pal)
    # Range for adding elements to list according to iterating "I"
    for i in range(l):
        check.insert(0, pal[i])
    # If opposite of input is same as input
    if check == pal:
        return True # Input is palindrome
    else:
        return False

def largest_digits(inp):
    res = 0
    for i in range(0,inp):
        res += 9 * (10**i)
    return res
