def panadrome_num(st):
    s="abcdefghijklmnopqrstuvwxyz"
    for char in s:
        if char not in st.lower():
            return("non panagram")
    else:
        return("panagaram")
str=input("enter the string")
print(panadrome_num(str))