#highest value given by user
'''a=int(input("Enter a number: "))
b=int(input("Enter a number: "))
if(a>b):
    print("a")
else:
    print("b")'''

#even or odd:
'''a=int(input("Enter a number: "))
if(a%2==0):
    print("even")
else:
    print("odd")'''

#highest value of three givwen by user:
'''a=int(input("Enter a number: "))
b=int(input("Enter a number: "))
c=int(input("Enter a number: "))
if(a>b) and (a>c):
    print("a")
elif(b>a) and (b>c):
    print("b")
else:
    print("c")'''

#lowest value of two numbers
'''a=int(input("Enter a number: "))
b=int(input("Enter a number: "))
if(a<b):
    print("a")
else:
    print("b")'''

#smallest of three numbers:
'''a=int(input("Enter a number a: "))
b=int(input("Enter a number b: "))
c=int(input("Enter a number c: "))
if(a<b) and (a<c):
    print("a")
elif(b<a) and (b<c):
    print("b")
else:
    print("c")'''

#pgm to check given number is 1 B/W 100 ?
'''a=int(input("Enter a number a: "))
if(a<101):
    print("Yes")
else:
    print("no")'''

#to take a single digit number from keyboard and print the value in english word?
'''a=int(input("Enter a number a: "))
words=["ZERO","ONE","TWO","THREE","FOUR","FIVE","SIX","SEVEN","EIGHT","NINE","TEN"]
print(words[a])'''

#nested if
'''name=input("Enter a  name: ")
Quali=input("enter the Quali")
year=int(input("enter the year: "))
percentage=int(input("enter the percentage: "))
if("Quali"=="btech") and ("Quali"=="mtech"):
    print("error")
elif(year==1917) and (year==1918):
    print(year)
elif(35<0) and (50>35):
    print("avg")
elif(50<75) and (90>75):
    print("good")
else:
    print("Submit")'''

#pgm display the num 1 to 10 using for loop?
'''for i in range(1,11):
    print(i)'''

#pgm even numbers 10 and below 10
'''for i in range(1,10):
    if(i%2==0):
        print(i)

for i in range(10,1,-2):
   print(i)'''

#pgm to get only even number 10,20,11,14,13,16,30
'''list=[10,20,11,14,13,16,30]
for i in list:
    if(i%2==0):
       print(i)'''

#display odd numbers b/w 10 and 20 in given list in above list
'''list=[10,20,11,14,13,16,30]
for i in list:
    if(i%2==1):
        print(i)'''

#pgm to display the missed values in b/w 10 and 20 in above list
'''list=[10,20,11,14,13,16,30]
for i in range(10,20):
    if i not in list:
        print(i)'''

#pgm to display 8th table by using for loop
'''for i in range(1,11):
    print("8 *",i,"=",8*i)'''

#pgm to display the table as per he user requirement
a=int(input("enter the number: "))
for i in range(1,11):
    print(a,"*", i,"=",a*i)

#pgm to diplay the missed number which is divisible by 3 in given list (12,11,18,9,6,4,8)
'''a=[12,11,18,9,6,4,8]
for i in a:
    if(i%3==0):
        print(i)'''

#pgm divisble by 3 and but not divisble by 5
'''a=int(input("Enter a num:  "))
if(a%3==0):
    print("Divisible by 3")
elif(a%5==0):
    print("Divisible by 5")
else:
    print("No")'''

#pgm to display the given number is prime number or not.
'''a=int(input("Enter a number:  "))
for i in range(2,a):
    if(a%i==0):
        print("not prime")
        break
    else:
        print("prime")'''


