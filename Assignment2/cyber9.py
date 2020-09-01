import sys

n=int(sys.argv[1])
a=0
b=1
for i in range(0,n):
    c=a+b
    b=a
    a=c
    print(a)
