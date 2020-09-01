def upperlower(str):
    c = 0
    x = 0
    for i in range(len(str)):
        if (str[i] >= 'A' and str[i] <= 'Z'):
            c += 1


        elif (str[i] >= 'a' and str[i] <= 'z'):
            x += 1
    return (c, x)


str = input("enter the string")
print(upperlower(str))


















