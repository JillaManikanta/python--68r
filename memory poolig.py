

#STRING INDEXING
str1='Manikanta'
print(str1[3])


#SLICING
str2="Manikanta"
print(str2[0:3])



#SET
set1={3}
a=set()
print(set1)
print(type(a))
set3=(1,5.4,True,False,None,(1,2,3,),'sai')
print(set3)



#INTEGER INTERNING OUTSIDE THE RANGE
x=300
y=300
print(x == y) #SAME VALUE
print(x is y)  #DIFFERENT MEMORY LOCATION
#---------------------------------------------

#STRING INTERNING WITH IDENTIFIERS
s1='python'
s2='python'
print(s1==s2)
print(s1 is s2)

s3='py' + 'thon'
print(s1 is s3)
#--------------------------


#STRING CREATED AT RUNTIME
s4="".join(['py','thon'])
print(s4)
print(s1 is s4)