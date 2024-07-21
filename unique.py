def unique_list(l): 
    x = []
    
    for a in l: 
        if a not in x: 
            x.append(a)
    return x
my_list = []
n = int(input("Enter number of elements : "))

for i in range(0, n):
	element = int(input())
	my_list.append(element) 

print(unique_list(my_list))
