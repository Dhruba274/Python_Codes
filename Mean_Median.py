import numpy as np

def find_mean(elements):
    return np.mean(elements)

def find_median(elements):
    sorted_elements = np.sort(elements)
    n = len(sorted_elements)
    
    if n % 2 == 0:
        median = (sorted_elements[n//2 - 1] + sorted_elements[n//2]) / 2
    else:
        median = sorted_elements[n//2]
    
    return median

# Example usage
elements = [1, 3, 5, 7, 9]
mean = find_mean(elements)
median = find_median(elements)

print(f'Mean: {mean}')
print(f'Median: {median}')