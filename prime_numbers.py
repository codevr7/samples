# prime numbers
def is_prime(n):
    for p in range(2, n - 1):
        if n % p == 0:
            return False
    return True

