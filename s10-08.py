'''s={10,20,30}
s.add(40)
print(s)'''

'''s={10,20,30}
l={40,50,60}
s.update(l)
print(s)'''

'''s={50,20,30}
l={40,50,10}
s.update(l,range(4))
print(s)'''

'''s={10,20,30}
s1=s.copy()
print(s1)'''

'''s={10,20,30}
s.pop()
print(s)'''

'''s={10,20,30,40,50,60}
s.discard(50)
print(s)'''

'''s={10,20,30,40,50,60}
s.remove(40)
print(s)'''

#pgm to eliminate duplicate element in the set:
'''s={10,20,30,40,50,60}
l={50,60,70,80,90,10}
s.update(l)
print(s)'''

#pgm to print diff vowels present in the given word given by the user set method:
'''s={}
a=input("Enter a word: ")
vowels= "aeiou"
for i in vowels:
    print(s,i,a.lower().count(i))'''

#find the biggest value of three numbers using lambda function:
'''s=lambda a,b,c: max(a,b,c)
print(s(3,8,7))'''

#functions:
#Creating a function
#in python a function is defined using the def keyword:
'''def my_function():
    print("i am sairam")'''

#craeting a function:
'''def qurd():
    print("i am sai")
qurd()'''

#Arguments
#Information can be passed into functions as arguments.
#Arguments are specified after the function name, inside the parentheses. You can add as many arguments as you want, just separate them with a comma.
#positional arguments:
'''def sai(fname):
    print(fname + "python")
sai("a")
sai("b")
sai("c")'''

'''def sai(fname,lname):
    print(fname + lname + "btech")
sai(fname="a",lname="b")
sai(fname="c",lname="d")'''

'''def sai():
    a=int(input("enter a value:"))
    b=int(input("enter a value:"))
    if(a>b):
        print(a)
    else:
        print(b)
sai()'''


'''def sai():
    list=[1,2,3,4,5,6,7,8,9]
    for i in list:
        print(i,end=" ")
sai()'''


'''def func(name,age):
    print("I am" +" " +name +" "+ "my age is"+ " "+ age)
func("ram","9")'''

#keyword arguments:
'''def func(child1,child2,child3):
    print("The third child name is "+" "+child3)
func(child1="apple",child2="popaya",child3="mango")'''

'''if you change order won't change the result '''
'''def sai(name,age):
    print(name + age)
sai(age="9",name="a") or sai(name="a",age="9")'''

#Default parameter value:
#If we call the function without argument, it uses the default value:
'''def sai(name="c"):
    print("My name is" + name)
sai("a")
sai("b")
sai()
sai("d")'''

#Return values:
#To let a function return a value, use the return statement:
'''def sai(x):
    return 3*x
print(sai(2))
print(sai(3))
print(sai(2))

def sai(i):
    return 65+i
print(sai(1))
print(sai(2))
print(sai(3))'''

#varible length argument (or) Arbitary Keyword arguments:
'''def sai(*ram):
    print("My youngest child is"+" "+ram[3])
sai("a","b","c","d")

def sai(*list):
    print("value is"+" "+list[3])
sai("a","b","c","d","e")'''

#varible keyword arguments (or) Arbitrary Keyword Arguments, **kwargs
#If the number of keyword arguments is unknown, add a double ** before the parameter name:
'''def sai(**kids):
    print("My last name is"+" "+kids["fname"])
sai(fname="a",lname="b")'''
