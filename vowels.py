str=str(input("enter a string"))
newstr=" "
for ch in str:
    if ch=="A"or ch=="E" or ch=="I" or ch=="O"or ch=="U":
        newstr+="@"
    elif ch=="a" or ch=="e" or ch=="i" or ch=="o" or ch=="u":
        newstr+="@"
    else:
        newstr+=ch
print(newstr)
