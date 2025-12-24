n=1234
sum=0
while n>0:
    k=n%10
    sum+=k
    n=n//10
print(sum)


n=34562
even=0
odd=0
while n>0:
    k=n%10
    if k%2==0:
        even+=1
    else:
        odd+=1
    n=n//10
print(even,odd)

    

m="python"
k=""
for i in range(len(m)-1,-1,-1):
    k+=m[i]
print(k)
