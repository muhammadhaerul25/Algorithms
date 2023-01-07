from math import sqrt

def getDivisors(n):
    divisors = []
    for i in range(1, int(sqrt(n))+1):
        if n % i == 0:
            divisors.append(i)
            if i*i != n:
                divisors.append(n // i)
    return divisors

print(sorted(getDivisors(10)))
