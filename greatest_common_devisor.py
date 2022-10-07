#Program get Greatest Common Devisor (GCD) using for loop

m = int(input())
n = int(input())

def getGCD(m, n):
  fpb = 0
  for i in range(1, max(m, n)+1):
    if (m % i == 0 and n % i == 0):
      fpb = i
  return fpb

print(f'FPB ({m}, {n}) = {getGCD(m, n)}')