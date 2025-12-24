i=1
while i<=10:
    print(i)
    i+=1

i=1
sum=0
while i<=20:
    sum+=i
    i+=1
print(sum)
    

i=1
list1=[]
while i<=50:
    if i%2==0:
        list1+=[i]
    i+=1
print(list1)

n=int(input("enter the n value: "))
i=1
while i<=10:
    print(f"{n}*{i}={n*i}")
    i+=1