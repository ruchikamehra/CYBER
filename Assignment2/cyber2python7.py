n = int(input("enter the value for n"))
lis = []
tup = ()

for i in range(1, n+1):
    c = 0
    for j in range(1,n+1):
        if (i % j == 0):
            c = c + 1
    if (c == 2):
        tup = (i, "prime")
    else:
        tup = (i, "non prime")
    lis.append(tup)
print(lis)

