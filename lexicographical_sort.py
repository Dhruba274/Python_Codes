# Take user input and split it into a list on the hyphen ("-") separator creating a list named 'items'
# Take user input and split it a list based on the hyphen-") separator creating a list named 'items'
items = input("Enter hyphen-separated sequence of: ").split('-')

# Sort the elements in the 'items' list in lexicographical order (alphabetical and numerical sorting)
items.sort()

# Join the sorted elements in the 'items' list using the hyphen ("-") separator and print the resulting string
print("Sorted:")
print('-'.join(items))