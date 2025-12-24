#Types of scope 
#   there are 4 type of scope they are:
#      1.Local Scope
#      2.Global Scope
#      3.Non-Local Scope
#      4.Bulid-IN scope



def mani():
    mes="virat"
    print(mes)
mani()



#GLOBAL SCOPE

msg="mani"
def mani():
    print(msg)
mani()


#Write a program to print your surname as 
# the global variable and your as the local variable:

msg="jilla"
def mani():
    m="manikanta"
    print(msg,m)
mani()


msg=10
def mani():
    global msg
    msg+=1
    print(msg)
mani()
print(msg)




#Write the problem and take the "Hello" as the global variable and take the "world" as 
# the local variable that inside the string function and output should me "Hello World"

m="Hello "
def mani():
    global m
    m=m+"World"
mani()
print(m)



# NON LOCAL:

def mani():
    var="mani"
    def nani():
        print(var)
    nani()
mani()


def mani():
    var="mani"
    def nani():
       var="nani"
       print(var)
    print(var)
    nani()
mani()




def mani():
    var="mani"
    def nani():
        nonlocal var
        var="nani"
        print(var)
    nani()
    print(var)
mani()



# BUILD IN:


print=10


list=[1,2,3,4,5]
len=10
print(len(list))




n=5
sq=n*n
m=str(n)
n=str(sq)
if m.endswith(n):
    print("autographic")
else:
    print("not autographic")