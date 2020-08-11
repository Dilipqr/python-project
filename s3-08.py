#Display the numbers 1 to 10 by using while loop.
'''i=1
while(i<=10):
    i=i+1
    print(i,end=" ")'''

#pgm  display the even numbers in between 10 and 20 including 10 and 20 also
'''a=8
while(a<20):
    a=a+2
    print(a)'''

#pgm to find the missing value in the list=[1,2,3,4,5,6,9,10] in any loop.
'''list=[1,2,3,4,5,6,9,10]
for i in range(1,10):
      if i not in list:
           print(i)'''

#pgm to find the missing even value in the list=[1,2,3,4,5,6,9,10
'''list=[1,2,3,4,5,6,9,10]
for i in range (1,10):
    if i not in list:
       if(i%2==0):
        print(i)'''

#pgm to dispaly table by using while loop.
'''a=1
while(a<=10):
    print(2,"*",a,"=",2*a)
    a=a+1
    continue'''

#pgm to get the values less than or equal to 10 list=[4,6,19,3,17,10,55,13]
'''list=[4,6,19,3,17,10,55,13]
for i in range(1,10):
    if i not in list:
        print(i)'''

#pgm to display the numbers from 1 to 10  except from 3,5,7.
for i in range(1,11):
    if(i==3):
        continue
    elif(i==5):
        continue
    elif(i==7):
        continue
    print(i,end=" ")