def centi_to_faren(c):
    f=(9*c/5)+32
    return f
def faren_to_centi(f):
    c=((f-32)*5)/9
    return c
    
f=centi_to_faren(26)
print(f)
c=faren_to_centi(78)
print(c)