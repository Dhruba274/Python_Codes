def check_prime(n):
    flag=1
    if n==0 or n==1 or n==2:
        print("prime number")
    else:
        for i in range(2,n-1):
            if  (n % i) == 0:
                flag = 0
                break
    if  flag == 1 :
        print("The number ",n," is prime")
    else:
        print("The number ",n," is not a prime")
        
def prime_range(n):
    for i in range (10):
        check_prime(i+2) # to exclude 0 and 1 from the list of numbers.

prime_range(10)
        