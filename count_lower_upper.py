def count_low_up(s):
    low = 0
    up = 0
    for c in s:
        if ord('a') <= ord(c) <= ord('z'):
            low += 1
        elif ord('A') <= ord(c) <= ord('Z'):
            up += 1
        
    return low, up
print(count_low_up("Hello World")) # (2, 8)
#print(ord('a'))