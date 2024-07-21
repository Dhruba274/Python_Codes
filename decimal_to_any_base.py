# Define a function to convert a decimal number to a number of a given base b
def decimal_to_base(n, b):
  
  result = ""
  # Loop until n becomes zero
  while n > 0:
    # Find the remainder of n divided by b
    remainder = n % b
    
    if remainder < 10:
      
      char = str(remainder)
    else:
      
      char = chr(ord('A') + remainder - 10)
    # Append the character to the result
    result = char + result
    
    n = n // b
  # Return the result
  return result

print(decimal_to_base(10, 2)) # Output: 1010
print(decimal_to_base(255, 16)) # Output: FF
print(decimal_to_base(100, 8)) # Output: 144
