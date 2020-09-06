def summer_69(li):
    sum=0
    sumx=0
    sum1=0
    m=0
    n=0
    if(li==[]):
        return 0
    else:
        for i in range(0,l):
            sum=sum+li[i]
            if(li[i]==6):
                m=i
        for i in range(m,l):
            if(li[i]==9):
                n=i
        if m==0 and n==0:
           return sum
        else:
            for i in range(m,n+1):
                sum1=sum1+li[i]
    sumx=sum-sum1
    return (sumx)

l = int(input("enter the number"))
lis = []
for i in range(0, l):
    x = int(input())
    lis.append(x)
print(summer_69(lis))