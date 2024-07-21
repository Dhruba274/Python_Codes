def unit_bll(unit):
    if unit<=200:
        return unit*.50
    elif (unit>200 and unit<=400):
        return (100+(unit-200)*.65)
    elif(unit>400 and unit <=600):
        return (250+(unit-400)*.85)
    else:
        return (425+(unit-600)*1.25)
    
# Testing the function
print(unit_bll(250))