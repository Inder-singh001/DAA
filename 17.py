print("Inderpreet Singh")
print("2104118")
print("\n")

def brute_force(text, pattern):
    n = len(text)
    m = len(pattern)
    for i in range(n - m + 1):
        j = 0
        while j < m and text[i + j] == pattern[j]:
            j += 1
        if j == m:
            return i
    return -1

def rabin_karp(text, pattern):
    n = len(text)
    m = len(pattern)
    pattern_hash = hash(pattern)
    for i in range(n - m + 1):
        text_hash = hash(text[i:i + m])
        if text_hash == pattern_hash and text[i:i + m] == pattern:
            return i
    return -1

def compute_prefix_table(pattern):
    m = len(pattern)
    prefix_table = [0] * m
    j = 0
    for i in range(1, m):
        while j > 0 and pattern[i] != pattern[j]:
            j = prefix_table[j - 1]
        if pattern[i] == pattern[j]:
            j += 1
        prefix_table[i] = j
    return prefix_table

def kmp(text, pattern):
    n = len(text)
    m = len(pattern)
    prefix_table = compute_prefix_table(pattern)
    j = 0
    for i in range(n):
        while j > 0 and text[i] != pattern[j]:
            j = prefix_table[j - 1]
        if text[i] == pattern[j]:
            j += 1
        if j == m:
            return i - m + 1
    return -1

def precompute_bad_character_table(pattern):
    m = len(pattern)
    bad_char = [-1] * 256
    for i in range(m):
        bad_char[ord(pattern[i])] = i
    return bad_char

def precompute_good_suffix_table(pattern):
    m = len(pattern)
    suffix = [0] * (m + 1)
    j = m
    for i in range(m, -1, -1):
        while j < m and pattern[i:i + 1] != pattern[j:j + 1]:
            j = suffix[j + 1]
        if pattern[i:i + 1] == pattern[j:j + 1]:
            j -= 1
        suffix[i] = j
    return suffix

def boyer_moore(text, pattern):
    n = len(text)
    m = len(pattern)
    bad_char = precompute_bad_character_table(pattern)
    good_suffix = precompute_good_suffix_table(pattern)
    i = 0
    while i <= n - m:
        j = m - 1
        while j >= 0 and pattern[j] == text[i + j]:
            j -= 1
        if j < 0:
            return i
        max_shift_bad_char = j - bad_char[ord(text[i + j])]
        max_shift_good_suffix = 0
        if j < m - 1:
            max_shift_good_suffix = good_suffix[j + 1]
        i += max(max_shift_bad_char, max_shift_good_suffix)
    return -1


text = "ABABCABABCDABCDABDE"
pattern = "ABCD"

print(f"Brute Force: Pattern found at index ", brute_force(text, pattern))
print(f"Rabin-Karp: Pattern found at index ",rabin_karp(text, pattern))
print(f"KMP: Pattern found at index ", kmp(text, pattern))
print(f"Boyer-Moore: Pattern found at index ", boyer_moore(text, pattern))