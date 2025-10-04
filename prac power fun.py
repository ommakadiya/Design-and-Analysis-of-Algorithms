def power(x,n):
    if n == 0:
        return 1
    if n%2==0:
        return power(x,n/2)*power(x,n/2)
    else:
        return x*power(x,n/2)*power(x,n/2)


x=5
n=3
print(f"{x}^{n} =",power(x,n))

# def power(x, n):
#     if n == 0:
#         return 1
#     elif n % 2 == 0:
#         half = power(x, n // 2)
#         return half * half
#     else:
#         half = power(x, n // 2)
#         return x * half * half

# x = 5
# n = 3
# print(f"{x}^{n} =", power(x, n))