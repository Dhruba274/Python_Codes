def move_duplicates_to_end(lst):
    # Create an empty list to store non-duplicate elements
    non_duplicates = []
    duplicate=[]
    
    # Iterate through the input list
    for i in lst:
        # If the element is not in the non-duplicates list, add it
        if i not in non_duplicates:
            non_duplicates.append(i)
        # If the element is already in the non-duplicates list,
        # it is a duplicate, so remove it from the input list
        # and continue to the next iteration
        else:
            duplicate.append(i)
            
    # Concatenate the non-duplicates list with the remaining elements
    # of the input list to get the final result
    result = non_duplicates + duplicate
    
    return result

# Test the function
lst = [2, 3, 3, 1, 1, 5, 6, 6, 7, 8, 8, 9]
print(move_duplicates_to_end(lst)) # Output: [2, 3, 1, 5, 7, 6, 8, 9, 3, 1, 6, 8]