def matrix_chain_multiplication(d):
    n = len(d) - 1
    m = [[0] * n for _ in range(n)]

    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            m[i][j] = float('inf')
            for k in range(i, j):
                q = m[i][k] + m[k+1][j] + d[i] * d[k+1] * d[j+1]
                if q < m[i][j]:
                    m[i][j] = q
    return m[0][n-1]

d = [10, 20, 30, 40, 30]
print("Minimum number of multiplications is", matrix_chain_multiplication(d))