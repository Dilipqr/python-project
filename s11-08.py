'''a=int(input("Enter a number:"))
b=int(input("Enter a number:"))
if a>b:
    print(a)
else:
    print(b)'''

'''s=lambda a:a*a
s(2)'''

'''def sai(a):
    return a*a
sai(3)'''

#user defined functions:
'''def sai(x):
    return(lambda y: x+y)
a=sai(2)
print(a(2))

def sai(x):
    return (lambda y:x+y)
a=sai(2)
print(a(2))
b=sai(2)
print(b(2))'''

'''def ram(x):
    return lambda y:x+y
s=ram(2)
print(s(2))'''

#filter(): we use set,list,tuple: #SYNTAX: filter(function(lambda),iterables)
'''sai=[1,2,3,4,5,6]
ram=list(filter(lambda a:(a%2==0),sai))
print(ram)

a=[1,2,3,4,5,6,7,8]
b=tuple(filter(lambda c:c%2==1,a))
print(b)

a=[1,2,3,4]
b=set(filter(lambda c:(c%2==0),a))
print(b)'''

#map(function,iterable)
'''a=[1,2,3,4,5,6,7,8,9]
b=list(map(lambda c:(c%2==0),a))
print(b)'''

#reduce(function,sequence) It will print one output after another
'''from functools import reduce
reduce(lambda a,b: a+b,[2,3,4])

from functools import reduce
reduce(lambda a,b: a-b,[14,5])'''

#algebra
'''s=lambda a:a*a
s(2)

s=lambda x,y: 2*x+3*y
s(2,3)

s=lambda a,b: (a+b)**2 (**)power
s(2,2)'''

#methods:
#instance methods:

'''class sai:

    school = "shiridi"  #static varible students in shiridi :

    def __init__(self,m1,m2,m3):
        self.m1=m1    #instance varibles
        self.m2=m2
        self.m3=m3

    def avg(self):     #method
        return (self.m1 + self.m2 + self.m3)/3

    #def get_m1(self):             #Assers
    #    return self.m1

    #def set_m1(self,value):       # mutators  #modifity the value we use set
    #     self.m1=value


s1 = sai(2,3,4)    #m1,m2,m3
s2 = sai(4,5,9)     #m1,m2,m3
print(s1.m1)
print(s1.m2)
print(s1.m3)
print(s1.avg())
print(s2.m1)
print(s2.m2)
print(s2.m3)
print(s2.avg())'''

#Example-2

'''class sai:

     school="shiridi"

     def  __init__(self,m1,m2):
         self.m1=m1
         self.m2=m2

     def avg(self):
         return (self.m1 + self.m2)/2


s1=sai(2,2)
s2=sai(9,9)
print(s1.m1)
print(s1.m2)
print(s1.avg())
print(s2.m1)
print(s2.m2)
print(s2.avg())'''


#class method:
#example-1
'''class sai:
    school = "shiridi"

    def __init__(self, m1, m2):
        self.m1 = m1
        self.m2 = m2

    def avg(self):
        return (self.m1 + self.m2) / 2

    @classmethod
    def getschool(cls):
        return cls.school

s1 = sai(2, 2)
s2 = sai(9, 9)
print(s1.m1)
print(s1.m2)
print(s1.avg())
print(s2.m1)
print(s2.m2)
print(s2.avg())

print(sai.getschool())'''

#example-2
'''class sai:
    ram="shiridi"


    @classmethod
    def ram(cls):
        return cls.school


print(sai.ram())'''

#static method:
'''class sai:
   ram="shiridi"


    @staticmethod
    def ram():
        print("This is student class")


sai.ram()'''


'''class sai:

    school="shiridi"

    def __init__(self,m1,m2):
        self.m1=m1
        self.m2=m2

    def sum(self):
        return (self.m1+self.m2)

    @classmethod
    def getschool(cls):
        return cls.school
    @staticmethod
    def ram():
        print("I am sai")

s1=sai(2,3)
s2=sai(2,4)
print(s1.m1,end=" ")
print(s1.m2,end=" ")
print(s1.sum())
print(s2.m1,end=" ")
print(s2.m2,end=" ")
print(s2.sum())

print(sai.getschool())
sai.ram()'''

#Instance class:
class sai:



    def __init__(self):
        self.mil=10
        self.brand="MUSTUNG GT"

s1=sai()
s2=sai()
s1.mil=8

print(s1.mil,s1.brand)
print(s2.mil,s2.brand)