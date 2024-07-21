def is_pangram(s):
    alphabet = set('abcdefghijklmnopqrstuvwxyz')
    s = set(s.lower())
    return alphabet.issubset(s)

# Test the function
print(is_pangram("The quick brown fox jumps over the lazy dog."))