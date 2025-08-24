n=int(input("enter the number:"))
f=0
s=1
fin=[]
for i in range(n):
    fin.append(f)
    f,s=s,f+s
print(fin)    


