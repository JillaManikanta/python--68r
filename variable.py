x=10
print('x=',x)


y='Mani'
print('y=',y)

z=2.5
print('z=',z)


print(type(x))

print(type(y))

print(type(z))

name='Manikanta'
age=21
height=5.6
is_working=True
address="yadagirigutta,Hyderabad"


print(name)
print(age)
print(height)
print(is_working)
print(address)


print(type(name))
print(type(age))
print(type(height))
print(type(is_working))
print(type(address))



m="hello world. welcome to python. glad you came"
sentences=m.split('.')
print(sentences)
list1=[]
for i in sentences:
    sen=i[0].upper()+i[1:]
    list1.append(sentences)
result = '. '.join(list1)
print(result)
