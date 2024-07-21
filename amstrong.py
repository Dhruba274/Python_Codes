def is_armstrong(n):
    # Convert the number to a string
    n_str = str(n)
    
    # Calculate the sum of the digits raised to the power of the number of digits
    sum_of_digits = sum(int(digit) ** len(n_str) for digit in n_str)
    
    # Check if the sum is equal to the original number
    return sum_of_digits == n

# Test the function
num = 153
if is_armstrong(num):
    print(f"{num} is an Armstrong number")
else:
    print(f"{num} is not an Armstrong number")