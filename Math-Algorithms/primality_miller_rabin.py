import random

def is_prime(n, k = 5):
    # Base case
    if n <= 1 or n == 4:
        return False
    if n <= 3:
        return True

    # Find a number d such that n-1 = 2^r * d
    d = n - 1
    r = 0
    while d % 2 == 0:
        d //= 2
        r += 1
    
    # Iterate k times
    for _ in range(k):
        a = random.randint(2, n-2)
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            continue

        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True

# Example usage
print(is_prime(11)) # True
print(is_prime(12)) # False


#The time complexity of the Miller-Rabin primality test is O(k log^3 n)