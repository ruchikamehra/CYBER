def has_33(li):
    m=0
    for i in range(0,l,1):
        if li[i]==3:
            m=i
            for i in range(m,l,1):
                if (li[i]==3 and li[m+1]==3):
                    return("true")
                else:
                    return("false")
l = int(input("enter the number"))
lis = []
for i in range(0, l):
    x = int(input())
    lis.append(x)
print(lis)
print(has_33(lis))