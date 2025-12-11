def kmp(str, pat):
    M = len(pat)
    N = len(str)
    i = 0
    j = 0
    while i < N and j < M:
        if str[i] == pat[j]:
            i += 1
            j += 1
        else:
            i = i - j + 1
            j = 0
    if j == M:
        return i - j
    else:
        return -1

str = "ABABDABACDABABCABAB"
pat = "ABABCABAB"
print(kmp(str, pat))
