def primeno(a):
    x=0
    for i in range(0,a):
         c=0
         for j in range(1,a):
            if i%j==0:
                c=c+1
         if c==2:
              x=x+1

    return x
n=int(input("enter the number"))
print(primeno(n))
