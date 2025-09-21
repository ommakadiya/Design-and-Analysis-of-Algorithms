def longest_common_subsequence(str1, str2):
    m = len(str1)
    n = len(str2)
    l = [[0 for i in  range (n + 1)]for j in  range (m + 1)]
    for i in range(1, n+1):
        for j in range(1, m+1):
            if(str1[i - 1]==str2[j - 1]):
                l[i][j] = 1 + l[i - 1][j - 1]
            else:
                l[i][j] = max(l[i][j - 1], l[i - 1][j])
    return l[n][m]

str1 = input("Enter First String: ")
str2 = input("Enter Second String: ")
res = longest_common_subsequence(str1, str2)
print(res)