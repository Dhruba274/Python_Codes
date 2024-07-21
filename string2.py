def mid_start(s1,s2):
    mid=len(s1)//2
    midd=len(s2)//2
    s3=s1[0]+s1[mid]+s1[len(s1)-1]+s2[0]+s2[midd]+s2[len(s2)-1]
    return s3
s1="Hello"
s2="World"
stri=mid_start(s1,s2)
print(stri)
