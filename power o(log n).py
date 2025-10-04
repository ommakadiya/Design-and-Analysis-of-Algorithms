def optimized_power(base, exponent):  
    if exponent == 0:
        return 1
    temp = optimized_power(base, exponent // 2)
    if exponent % 2 == 0:
        return temp * temp
    else:
        return base * temp * temp

a = 2
b = 6
print(optimized_power(a, b))
