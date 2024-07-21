def fact(n):
    fact =1
    for i in range(n):
        fact *= (i+1)
    return fact
    
def add(n):
    sum=0
    if n<1:
        print("Input should be positive integer")
    else:
        for i in range(1,n+1):
            sum +=1/fact(i)
        return sum
print(add(3))
