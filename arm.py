n=int(input("enter the number:"))
sum=0
temp=n

while n>0:
    rem=n%10
    sum=sum+(rem*rem*rem)
    n=n//10
if(temp==sum):
    print("Yes")
else:
    print("No")