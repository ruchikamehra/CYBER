def lesser(a,b):
    if a%2==0 and b%2==0:
        min=a
        if min>b:
            min=b
        return min
    elif a%2!=0 or b%2!=0:
        max=a
        if max<b:
            max=b
        return (max)
x=int(input("enter the first number"))
y=int(input("enter the second number"))
print(lesser(x,y))
