def rabin_karp(text, pattern, base=256, prime=101):
    n = len(text)
    m = len(pattern)
    if m > n:
        return []
    pattern_hash = 0
    text_hash = 0
    h = 1 
    for _ in range(m - 1):
        h = (h * base) % prime
    for i in range(m):
        pattern_hash = (base * pattern_hash + ord(pattern[i])) % prime
        text_hash = (base * text_hash + ord(text[i])) % prime
    results = []
    for i in range(n - m + 1):
        if pattern_hash == text_hash:
            if text[i:i + m] == pattern:
                results.append(i)
        if i < n - m:
            text_hash = (base * (text_hash - ord(text[i]) * h) + ord(text[i + m])) % prime
            if text_hash < 0:
                text_hash += prime
    return results


string = "abababcd"
pattern = "abcd"
matches = rabin_karp(string, pattern)
print("Pattern found at indices:", matches)
