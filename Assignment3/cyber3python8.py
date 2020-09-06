def spy_game(li):
    c=0
    x=0
    for i in range(0,l):
          if(li[i]==0):
               c=c+1
               if c==2:
                    m=i
    for j in range(m,l):
          if li[j]==7:
                x=1
    if x==1:
         return("true")
    else:
        return("false")
l=int(input("enter the number"))
lis=[]
for i in range(0,l):
    x=int(input())
    lis.append(x)
print(spy_game(lis))
