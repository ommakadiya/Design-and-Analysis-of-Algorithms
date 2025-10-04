def recursive_power(base, exponent):  
    if exponent == 0:
        return 1
    else:
        if exponent < 0:
            exponent = abs(exponent)
            return 1 / recursive_power(base, exponent)
        else:
            return base * recursive_power(base, exponent - 1)

a = 2
b = 6
print(recursive_power(a, b))
