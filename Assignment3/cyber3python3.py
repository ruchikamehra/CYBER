def reversed_words(st):
    a=st.split()
    a=a[::-1]
    a=" ".join(a)
    return(a)
str=input("enter the string")
print(reversed_words(str))