# A function for finding next fibinooci number from a given number
def next_fib(fib):
    out = 1
    if fib == 1 or fib == 2:
        return 1
    complete = False
    times = 3
    while not complete:
        if fibin(times) >= fib:
            return times
            complete = True
        times += 1
    for j in range(1000):
        out = out*10

# A function for finding input index 
def fibin(num):
    if num == 1 or num == 2:
        return 1
    val_1 = 1
    val_2 = 1
    for i in range(1,num-1):
        val = val_1 + val_2
        val_1 = val_2
        val_2 = val
    return val

