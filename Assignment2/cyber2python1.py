def volume(r):
    v=4/3*3.14*(r**3)
    x=round(v,2)
    return x

r=int(input("enter the radius"))
print(volume(r))
