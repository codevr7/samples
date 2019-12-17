# Defining a function for input
def odd_one(n):
    convert = []# The list for converting word into number of letters
    check = []# The list for checking if word is odd
    final = []
    
    # Process of converting input to number of letters in each word
    for j in range(len(n)):
        convert.append(len(n[j]))
        start = convert[0]
        
    for k in range(len(convert)):
        for i in range(1,len(convert)):
            if start == convert[i]:
                check.append(convert[i])
        if len(check) == 0:
            final.append(start)
        if len(check) > 0:
            check = []
        convert.insert(len(convert), start)
        del convert[0]
        start = convert[0]

    if len(final) == 1:
        return True
    else:
        return False
