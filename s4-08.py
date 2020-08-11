#strings:
#It is surrounded by either single or double quotataion marks:

'''print(" sai ram")
print('sai')'''

'''a=("quadrant")
print(a)'''

#strings are arrays:
'''a=("python")
print(a[1])'''

#Slicing:
#you can return a range of characters by using the slice syntax:
'''a=("quadrantid")
print(a[4:7])'''

#Negative indexing
'''a=("sairam")
print(a[-4])'''

'''a=("quadrant resource")
print(a[-7:-4])'''

'''a=("dilip kumar")
print(a[3:9])

a=("quadrant resource")
print(a[-9:-4])'''

#length:
'''a=("quadrant resource")
print(len(a))'''

#strip :  o/p: (Remove quotes in string)
'''a=("dilip kumar athmakuri")
print(a.strip())'''

#lower:
'''a=("DILIP KUMAR")
print(a.lower())'''

#UPPER:
'''a=("dilip kumar athmakuri")
print(a.upper())'''

#replace:
'''a=("dilip kumar athmakuri")
print(a.replace("i","ia"))'''

#sprit() o/p: change the brackets
'''a=("dilip kumar athamkuri")
print(a.split(","))'''

#check string:
'''a="I am great devotee of om sai ram"
b="great" in a
print(b)'''

'''a="I am great devotee of om sai ram"
b="great" not in a
print(b)'''

#string concate:
#use (+) symbol:
'''a="sai"
b="ram"
c=a+b
print(c)

a="sai"
b="ram"
c=a+"  "+b
print(c)'''

#string Format():
'''a=36
b="my name is sai, I am {}"
print(b.format(a))

a=9
b=999
c=99.99
d=" i want {} pieces of item {} for {} dollars."
print(d.format(a,b,c))'''

#Escape character:
'''a=" I am dilip \"kumar\" athmakuri"
print(a)'''

#carrige return:
'''a="dilip\rkumar"
print(a)
o/p: kumar'''

#count:
'''a="dilipkumar"
b=a.count("a")
print(b)'''

#Index or find()
'''a=("dilip kumar athmakuri")
b=a.index("kumar")
print(b)
'''

#delete:
'''a=("Dilip kumar")
del a
print(a)'''

#replace:
'''a=("dilip kumar")
b=a.replace("dilip", "sai")
print(b)'''

Assignment:

#How to display the given string in ascending order:
'''a='python'
b=sorted(a)
print(b)'''

#How to display the given string in desecending order:
'''a='python'
b=" ".join(reversed(sorted(a)))
print(b)'''

#how to reeverse a string:
'''a='omsairam'
b=" ".join(reversed(a))
print(b)'''

