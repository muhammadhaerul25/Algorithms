def common_factors(num_set):
    common_factors = set()
    for i in range(2, min(num_set) + 1):
        if all(num % i == 0 for num in num_set):
            common_factors.add(i)
    return common_factors
