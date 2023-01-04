m = int(input('Input nilai m: '))

def hitung_fpb(x, y):
    if x > y:
        smaller = y
    else:
        smaller = x
    for i in range(1, smaller +1):
        if ((x % i == 0) and (y % i == 0)):
            fpb = i
    return fpb

himpunan = ''
jumlah = 0
for n in range(1, m):
    fpb = hitung_fpb(m, n)
    if fpb == 1:
        himpunan = himpunan + ' ' + str(n)
        jumlah = jumlah + 1
print('Himpunan :', himpunan)
print('Jumlah   : ', jumlah)
