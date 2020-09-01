x = int(input("enter the number"))
d = dict()
p=0
for i in range(1, x + 1, 1):
    c = 0
    for j in range(1, i + 1, 1):
        if (i % j == 0):
            c = c + 1
    if (c == 2):
        d[i] = 'prime'
    else:
        d[i]='non-prime'
print(d)
for i in range(1,x+1):
    if(d[i]=='non-prime'):
        del d[i]
        p=p+1
print(d)
print(p)
