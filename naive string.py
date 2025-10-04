def naive_string_match(text, pattern):
    n = len(text)
    m = len(pattern)
    positions = []  # store all match indices

    # Slide pattern over text
    for i in range(n - m + 1):
        match = True
        for j in range(m):
            if text[i + j] != pattern[j]:
                match = False
                break
        if match:
            positions.append(i)

    return positions


# Example usage
text = "ABABDABACDABABCABAB"
pattern = "ABABCABAB"
result = naive_string_match(text, pattern)

print("Pattern found at indices:", result)