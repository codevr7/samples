def largest(n):
    l = len(n)
    largest = n[0]
    for i in range(1, l):
        if n[i] > largest:
            largest = n[i]
    return largest
    
    
    
