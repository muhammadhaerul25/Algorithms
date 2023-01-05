def print_euclidean_algorithm(m, n):
    m1, n1 = 0, 0

    while n != 0:
        q = m // n
        r = m - n * q

        m1, n1 = m, n
        m, n = n, r

        print(f"{m1} = {n1}({q}) + {r}")

    if n1 < 0:
        n1 = n1 * (-1)

    print(f"\nGCD = {n1}")


m, n = map(int, input("Enter two numbers: ").split())
print_euclidean_algorithm(m, n)
