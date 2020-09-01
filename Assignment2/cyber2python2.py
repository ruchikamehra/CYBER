def numrange( num,x):
    c=0
    for i in range(num) :
        if(x==i):
            c=c+1
    if(c==1):
       print("yes")
    else :
        print("false")
num=int(input("enter the num"))
x=int(input("enter the x you want to check"))
numrange(num,x)
