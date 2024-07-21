# Define a function to check whether a number is a perfect number or not
def is_perfect(n):
  # Initialize a variable to store the sum of the proper divisors
  sum = 0
  # Loop from 1 to n-1
  for i in range(1, n):
    # If i is a divisor of n
    if n % i == 0:
      # Add i to the sum
      sum += i
  # Return True if the sum is equal to n, False otherwise
  return sum == n

# Test the function with some examples
print(is_perfect(6)) # Output: True
print(is_perfect(28)) # Output: True
print(is_perfect(15)) # Output: False
