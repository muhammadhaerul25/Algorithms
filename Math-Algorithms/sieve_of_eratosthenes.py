#Sieve of Eratosthenes
def sieveOfEratosThenes(n):
    eliminated = [False]*(n+1)
    primeList = []
    for i in range (2, n):
        if not eliminated[i]:
            primeList.append(i)
            j = i*i
            while j <= n:
                eliminated[j] = True
                j += i
    return primeList