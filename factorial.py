#Program get factorial using recursion function

n = int(input(''))

result = 1

def factorial(value):
  if value > 1:
    global result
    result = result * value
    factorial(value-1)

  elif value < 0:
    result = 'Undefined'

  return result  

print(str(n) + "! = " + str(factorial(n)))