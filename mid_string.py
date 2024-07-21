def append_in_middle(s1, s2):
    # Calculate the middle index of s1
    middle_index = len(s1) // 2
    
    # Append s2 in the middle of s1
    new_string = s1[:middle_index] + s2 + s1[middle_index:]
    
    return new_string

# Test the function
s1 = "Hello"
s2 = " World"
new_string = append_in_middle(s1, s2)
print(new_string) 