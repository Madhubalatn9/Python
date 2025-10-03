s=input("Enter the String:")
left=0
right=len(s)-1
isPal=True
while left<right:
    if s[left]!=s[right]:
         isPal=False
    left +=1
    right -=1
if(isPal):
   print("palindrome")
else:
   print("Not palindrome")