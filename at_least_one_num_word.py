def checkString(str):

    flag_l = False
    flag_n = False

    for i in str:
     
        
        if i in "abcdefghijklmnopqrstuvwxyz":
            flag_l = True
 
        if i in "0123456789":
            flag_n = True
     
 
    return flag_l and flag_n
 
 
# driver code
print(checkString('thishasboth29'))
print(checkString('7 Thala for a reason'))