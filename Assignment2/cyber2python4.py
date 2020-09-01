def unique(list):
    lis2 = []
    for i in lis1:
        if i not in lis2:
            lis2.append(i)
    return (lis2)


lis1 = []
l1 = int(input("enetr the numbers"))
for i in range(0, l1):
    x = int(input())
    lis1.append(x)
print(lis1)
print(unique(lis1))

