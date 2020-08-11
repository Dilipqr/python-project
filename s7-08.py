#A set is unordered and unindexed.sets are written in curly brackets.


'''a={"om","sai","ram"}
print(a)'''


'''a={"a","b","c"}
for i in a:
    print(i)'''



'''a={"dilip","sai","kumar"}
print("sai" in a)'''



#Once set is created, you cannot change the items, but you can add new items


#ADD
'''a={"quadrant""}
a.add("resource")
print(a)'''


#UPDATE
'''a={"cherry","mango","apple"}
a.update(["dilip","kumar","athmakuri"])
print(a)'''


#LEN
'''a={"a","b","c"}
print(len(a))'''


#we can not access items in a set by refering to an index,beacuse it is unordered.


#REMOVE
'''a={"a","b","c"}
a.remove("b")
print(a)'''


#DISCARD
'''a={"a","b","c"}
a.discard("a")
print(a)'''



#sets are unordered, so when using the pop() method, you will not know which item that gets removed


#POP
'''a={"a","b","c"}
b=a.pop()
print(b)
'''


#CLEAR
'''a={"a","b","c"}
a.clear()
print(a)'''


#DEl
'''a={"a","b","c"}
del a
print(a)'''



#join two sets:(union or update)


#UNION
'''set1={"a","b","c"}
set2={1,2,3}
set3=set1.union(set2)
print(set3)'''


#UPDATE
'''set1={"a","b","c"}
set2={1,2,3}
set1.update(set2)
print(set1)'''


#set()
'''a=set(("a","b","c"))
print(a)'''


#ADD
'''set1={"a","b","c"}
set1.add("d")
print(set1)'''


#COPY
'''set1={"a","b","c"}
set2=set1.copy()
print(set2)'''


#Difference
'''sai={"a","b","c"}
ram={"d","e","a"}
z=ram.difference(sai)
print(z)'''


#Diff_Update
'''sai={"a","b","c"}
ram={"d","e","a"}
z=sai.difference_update(ram)
print(z)'''


#INTERSECTION
'''a={"banana","mango","orange"}
b={"apple","banana","grapes"}
c=a.intersection(b)
print(c)'''


#UNION
'''a={"banana","mango","orange"}
b={"apple","banana","grapes"}
c=a.union(b)
print(c)'''


#Symmetric
'''a={"banana","mango","orange"}
b={"apple","banana","grapes"}
c=a.symmetric_difference(b)
print(c)'''


#Disjoint
'''a={"banana","mango","orange"}
b={"apple","cherry","grapes"}
c=a.isdisjoint(b)
print(c)'''


#issubset
'''x = {"a", "b", "c"}
y = {"f", "e", "d", "c", "b", "a"}
z=x.issubset(y)
print(z)'''


#update
'''a={"banana","mango","orange"}
b={"apple","cherry","grapes"}
a.update(b)
print(a)'''