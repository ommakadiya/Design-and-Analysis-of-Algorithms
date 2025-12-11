def sum(n):
    if n == 0:
        return 0
    elif n>0:
        return n + sum(n - 1)
    else:
        return n + sum(n + 1)
