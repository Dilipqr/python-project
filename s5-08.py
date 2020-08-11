#list is collection which is orederd and changeable:
#written is square brackets:
'''a=["x","y","z"]
print(a)'''

#Access items:
'''a=["x","y","z"]
print(a[1])'''

#negative indexing:
'''a=["x","y","z"]
print(a[-1])'''

#range of indexes:
#start from 01234 to 6
#6 value does not print
'''a=["a","b","c","d","e","f","g","h","i"]
print(a[4:6])

a=["a","b","c","d","e","f","g","h","i"]
print(a[:4])

a=["a","b","c","d","e","f","g","h","i"]
print(a[4:])

a=["a","b","c","d","e","f","g","h","i"]
print(a[-4:-1])'''

#cHANGE ITEM VALUE:
'''a=["a","b","c","d","e","f","g","h","i"]
a[2]="s"
print(a)'''

#Loop through list:
'''a=["a","b","c","d","e","f","g","h","i"]
for x in a:
    print(x,end=" ")'''

#if loop:
'''a=["a","b","c","d","e","f","g","h","i"]
if "b" in a:
    print("yes")
else:
    print("no")'''

#len()
'''a=["a","b","c","d","e","f","g","h","i"]
print(len(a))'''

#append()
#add item end of the list:
'''a=["a","b","c","d","e","f","g","h","i"]
a.append("j")
print(a)'''

#insert:
#Insert the specified value at specified position:
'''a=["a","b","c","d","e","f","g","h","i"]
a.insert(4,"j")
print(a)'''

#extend:
#add the specified element end of the list:
'''a=["a","b","c","d","e","f","g","h","i"]
a.extend([1,2])
print(a)'''

'''a=["a","b","c"]
a.extend([1,2,3])
print(a)'''

#remove:
'''a=["a","b","c","d","e","f","g","h","i"]
a.remove("c")
print(a)'''

#pop:
'''a=["a","b","c","d","e","f","g","h","i"]
a.pop()
print(a)'''

#delete:
'''a=["a","b","c","d","e","f","g","h","i"]
del a'''

#clear()
'''a=["a","b","c","d","e","f","g","h","i"]
a.clear()
print(a)'''

#list(): Constructor:
'''a=list(("a","b","c"))
print(a)'''

#copy:
'''a=["a","b","c"]
b=a.copy()
print(b)'''

#count()
'''a=["a","b","c","d","e","b","g","b","i"]
print(a.count("b"))'''

#index:
'''a=["a","b","c","d","e","f","g","h","i"]
print(a.index("a"))'''

#remove
'''a=["a","b","c","d","e","f","g","h","i"]
a.remove("g")
print(a)'''

#reverse
'''a=["a","b","c","d","e","f","g","h","i"]
a.reverse()
print(a)'''

#sort:
'''a=['i', 'h', 'g', 'f', 'e', 'd', 'c', 'b', 'a']
a.sort()
print(a)'''

#short hand syntax:
'''if (5>2): print("yes")
print("Yes") if 5 > 2 else print("No")'''

#given number is palindrome or not
'''a=input("enter a string: ")
b=(a[::-1])
if(a==b):
    print("palindrome")    #mom
else:
    print("Not palindrome")'''

#Fabonacci    
'''a=0
b=1
print(a)
print(b)                    #0 1 1 2 3 5 8 13 21 34 54 89
for i in range(0,10):
    c=a+b
    a=b
    b=c
    print(c)'''

#Given number is prime or not:
'''a=int(input("enter a number: "))
for i in range(2,a):
    if a%i==0:
        print("not prime")
        break
else:
    print("prime")
