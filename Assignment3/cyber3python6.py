def blackjack(li):
    sum=0
    sum1=0
    for i in range(0,l):
        sum=sum+li[i]
    if sum<=21:
        return(sum)
    elif(sum>21 and li[i]==11):
            sum1=sum-10
            if(sum1>21):
                return("BUST")
            else:
                return(sum1)
    elif sum>21 and li[i]!=11:
            return("BUST")
l = int(input("enter the number"))
lis = []
for i in range(0, l):
     x = int(input())
     lis.append(x)
print(blackjack(lis))