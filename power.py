def power(base, exponent):
    result = 1
    for i in range(exponent):
        result *= base
    return result

a = 3
b = 5
print(power(a, b))
