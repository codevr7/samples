# A function for finding the next prime number from an input
def next_prime(n):
    final = n
    if n%2 == 0:
        for i in range(n-1, 1,-1):
            if final%i == 0:
                final = final+1
            elif final%i != 0:
                return final
    else:
        print(final)
        
