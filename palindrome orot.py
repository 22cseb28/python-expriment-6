print("problems on string")
print("palindrome or not")
n=int(input("enter a number:"))
org=n
sum=0
while(n>0):
    a=n%10
    sum=sum*10+a
    n=n//10
    if(sum==org):
        print("it is a palindrome")
    else:
        print("it is not a palindrome")
            
