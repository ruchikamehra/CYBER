def almost_there(x):
    y=abs(x)
    if(y>=90 and y<=110 or y>=190 and y<=210):
        return("true")
    else:
        return("false")
n=int(input("enter the number"))
print(almost_there(n))