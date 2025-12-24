def funA():
    print("welcome to python programmming: ")
funA()


def funA():
    n=5
    for i in range(1,11):
        print(f"{n}*{i}={n*i}")
funA()



def funA():
    i=1
    list1=[]
    while i<=20:
        if i%2==0:
            list1+=[i]
        i+=1
    print(list1)
funA()


def funA():
    i=1
    while i<=10:
        print(i,end=" ")
        i+=1
funA()


def funA():
    sum=0
    for i in range(1,51):
        sum=sum+i
    print(sum)
funA()



def funA(n):
    if n%2==0:
        print("even")
    else:
        print("odd")
funA(5)


def funA(a,b,sum):
    sum=a+b
    print(sum)
funA(4,5,0)


def funA(s):
    print(s[::-1])
funA("mani")


def funA(n):
    for i in range(1,11):
        print(f"{n}*{i}={n*i}")
funA(5)


def funA(n,sum):
    sum=n*n
    return sum
print(funA(5,1))

import math
def funA(n,m,sum):
    sum=math.gcd(m,n)
    return sum
print(funA(12,18,0))
