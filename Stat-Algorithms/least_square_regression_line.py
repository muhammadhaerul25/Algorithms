# Enter your code here. Read input from STDIN. Print output to STDOUT
import statistics

def least_square_regression_line(x, y):
    x_mean = statistics.mean(x)
    y_mean = statistics.mean(y)
    x2_sum = 0
    xy_sum = 0
    for i in range(len(x)):
        x2_sum += x[i]**2
        xy_sum += x[i] * y[i]
    b = (len(x)*xy_sum - sum(x)*sum(y)) / (len(x)*x2_sum - sum(x)**2)
    a = y_mean - (b)*x_mean
    return a, b


math = []
stat = []

for i in range(5):
    x, y = map(int, input().split())
    math.append(x)
    stat.append(y)
    
a, b = least_square_regression_line(math, stat)

#when math = 80, what is the value of stat?
print(round(a + b*80, 3))