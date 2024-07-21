list1=[1,2,3,4,5,6,7]
list2=[1,2,3,5,4,7,8]
l1=len(list1)
l2=len(list2)
for i in range(l1):
    if list1[i]==list2[i]:
        continue
    else:
        print("The list unmatches index at",i)
        break