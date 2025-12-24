def add(*name):
    sum=0
    for i in name:
        sum=sum+i
    return sum
print(add(1,2,3,4))



def add(*name):
    sum=0
    for i in name:
        if i>sum:
            sum=i
    return sum
print(add(1,10,3,4))


def add(*name):
    sum=1
    for i in name:
        sum=sum*i
    return sum
print(add(1,2,3,4))



def add(*name):
    even=0
    odd=0
    for i in name:
        if i%2==0:
            even+=1
        else:
            odd+=1
    return even,odd
print(add(1,2,3,4,5))



def concat_strings(*args):
    return " ".join(args)
print(concat_strings("Hello", "Manikanta"))          # Output: Hello Manikanta
print(concat_strings("Python", "is", "awesome"))    # Output: Python is awesome
print(concat_strings("ACE", "Engineering", "College")) # Output: ACE Engineering College


def add(**name):
    for i,j in name.items():
        print(f"{i}: {j}")
add(name="mani",age=21,cls=15)



def add(**name):
    for i,j in name.items():
        print(f"{i}: {j}")
add(brand="mani",color="black",model=25)



def add(**names):
    for i,j in names.items():
        tatal=sum(names.values())
        return tatal
print(add(apple=21,banana=25))
print(add(apple=20,banana=21))




