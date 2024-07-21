
nterms = int(input("Enter the range of fibbonaci numbner "))

# first two terms
n1, n2 = 0, 1
count = 0
if nterms <= 0:
   print("Please enter a positive integer")
elif nterms == 1:
   print("Fibonacci sequence upto",nterms,":")
   print(n1)
# generating fibonacci sequence
else:
   print("Fibonacci sequence:")
   while count < nterms:
       print(n1)
       sum = n1 + n2
       n1 = n2
       n2 = sum
       count += 1