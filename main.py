import math


def count_of_variants(x):
    m = x // 10
    n = x % 10
    if n > m * 2:
        return 0
    elif n == m * 2 or n == m:
        return 1
    else:
        if x % 10 == 0:
            sum_of_combination = 1
            m -= 1
            n += 10
        else:
            sum_of_combination = 0
        while n <= 2 * m:
            if n > m:
                sum_of_combination += math.factorial(m) / (math.factorial(n - m) * math.factorial(2 * m - n))
                m -= 1
                n += 10
            else:
                sum_of_combination += math.factorial(m) / (math.factorial(n) * math.factorial(m - n))
                m -= 1
                n += 10
        return sum_of_combination


while True:
    try:
        k = int(input("Input int 'k': "))
        result = count_of_variants(k)
        print(result, "variants")
    except ValueError:
        print(" SYNTAX ERROR (k must be integer type)")
        continue
    break
