# Get the list and the range of indexes from the user
l = eval(input(" the list: "))
start = int(input("inputEnter start index: "))
stop = int(input("inputEnter stop index: "))

# Slice the list to get the desired range of elements
slice = l[start : stop + 1]

# Find the maximum and minimum values in the sliced list
mx = max(slice)
mi = min(slice)

# Print the maximum and minimum values
print("Maximum =", mx)
print("Minimum =", mi)