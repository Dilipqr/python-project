'''s=("apple","banana","cherry","orange","kiwi","melon","mango")
print(s[-5:-2])'''

'''x=("apple","banana","cherry")
y=list(x)
y[1]="kiwi"
x=tuple(y)
print(x)'''

'''x=("a","b","c")
y=list(x)
y[1]="d"
x=tuple(y)
print(x)'''

'''y="a","b","c","d"
x=list(y)
x[2]="s"
y=tuple(x)
print(y)'''

'''a=("om","sai","ram")
b=list(a)
b[1]="saisai"
a=tuple(b)
print(a)'''

'''a=("om","sai","ram")
for i in a:
    print(i)'''

'''x=("a","b","c")
for i in x:
    print(i)'''

'''a=("x","y","z")
if "x" in a:
    print("yes")
else:
    print("No")'''

'''a=(1,2,3)
b=list(a)
b.remove(2)
a=tuple(b)
print(b)'''

'''a=("om","sai","ram")
print(len(a))'''

'''a=(1,2,3)
b=list(a)
b.append(2)
a=tuple(b)
print(a)'''

'''a=("x",)
print(type(a))'''

'''a=("x","y","z")
print(a)
del a
print(a)'''

'''a=(1,2,3)
b=list(a)
b.extend('d')
a=tuple(b)
print(a)'''

'''a=("a","b","c")
b=a.index("b")
print(b)'''

#DICTIONARIES#

'''a={"brand":"ford","model":"mustang","year":2035}
print(a)'''

'''a={"brand":"ford","model":"mustang","year":2035}
b=a.get("brand")
print(b)'''

'''a={"brand":"ford","model":"mustang","year":2035}
a["year"]="2029"
print(a)'''

'''a={"brand":"ford","model":"mustang","year":2029}
for i in a:
    print(a[i])'''

'''a={"brand":"ford","model":"mustang","year":2035}
for i in a.values():
    print(i)'''

'''a={"brand":"ford","model":"mustang","year":2035}
for x,y in a.items():
    print(x,y)'''

'''a={"brand":"ford","model":"mustang","year":2035}
if "model" in a:
    print("yes")
else:
    print("No")'''

'''a={"brand":"ford","model":"mustang","year":2035}
print(len(a))'''

'''a={"brand":"ford","model":"mustang","year":2035}
a["colour"]="red"
print(a)'''

'''a={"brand":"ford","model":"mustang","year":2035}
a.pop("year")
print(a)'''

'''myfamily={"child1":{"name":"om","year":1864},"child2":{"name":"sai","year":1895},"child3":{"name":"Ram","year":1912}}
print(myfamily)'''

#comprehension:
'''list=[a*b for item in list if condition'''

'''s=[i*i for i in range(1,10)]'''

'''s=[2**i for i in range(1,6)]'''

'''s=[i for i in range(1,11) if i%2==0]'''

'''words=["python","Ml","D1"]
l=[w[o] for w in words]
print(l)'''

#write a pgm to display the unique vowels present in given keyword
'''x=input("Enter a string: ")
for i in x:
    if(i=="a" or i=="e" or i=="i" or i=="o" or i=="u"):
        print(i,end=" ")'''

#dictonary:
'''d={}
n=int(input("enter student number:  "))
i=1
while(i<=n):
        name=input("enter a student name: ")
        marks=input("enter %:")
        d[name]=marks
        i=i+1
print("name of students", "\t", "% of marks" )
for x in d:
    print(x,d[x])
    print(d)'''

