def pascal(n): 

    #test = []
    row = [1]
    #number = 0

    if n < 0:
        raise Exception('Invalid input ')

    for i in range(0,n):
        print(format_print(row, n))
        row = next(row)

def format_print(row , size):
    ret =  ''
    fix =  int((size - len(row)) / 2)
    
    for i in range(0, fix):
        ret += ' '

    for i in range(0, len(row)):
        ret += str(row[i])
        ret += ' '
        
    for i in range(0, fix):
        ret += ' '
    return ret

def next(row):
    ret = []
    current = 0
    nxt = 0
    for i in range(-1, len(row)):
        if i < 0:
            current = 0
        else:
            current = row[i]
            
        if i == len(row) - 1:
            nxt = 0
        else:
            nxt = row[i + 1]
        ret.append(current + nxt)
    return ret
     
