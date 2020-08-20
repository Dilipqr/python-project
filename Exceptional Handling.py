# Syntax Error:
# missing(:)  Ex: if(a<b): This is called compile time error

# Logical Error:
# It gives the output but it does not give correct output
# Eg:  2+3=4------Wrong output

# Run time error:
# All the code will be correct and output will be correct at some time the user cannot give correct input.
# Eg: 6/0----- user gives wrong input at that time gives an error.


'''a = 5
b = 2

try:
    print(a / b)  # Two types of statements: simple and critical
except Exception:
    print("Hey, you cannot divide a number by zero")

print("Bye")'''

#using Execption as e it will change the oyutput

'''a = 5
b = 0

try:
    print(a / b)  # Two types of statements: simple and critical
except Exception as e:
    print("Hey, you cannot divide a number by zero",e)

print("Bye")'''


#If we open any resource using try statement we will close that completion of work

'''a = 5
b = 0

try:
    print("resource open")
    print(a / b)  # Two types of statements: simple and critical
    print("resource closed")
except Exception as e:
    print("Hey, you cannot divide a number by zero",e)

print("Bye")'''

#We use finally statement  to close the resource:

'''a = 5
b = 2

try:
    print('resource open')
    print(a / b)

except Exception as e:
    print("Hey, you cannot divide a number by zero",e)

finally:
    print('resource closed')'''

#user input:

'''a = 5
b = 2

try:
    print('resource open')
    print(a / b)
    s=int(input("Enter a Number:  "))
    print(s)

except Exception as e:
    print("Hey, you cannot divide a number by zero",e)

finally:
    print('resource closed')'''


#It will shows different type of error:

'''a = 5
b = 2

s=int(input("Enter a Number:  "))
print(s)

try:
    print('resource open')
    print(a / b)


except Exception as e:
    print("Hey, you cannot divide a number by zero",e)

finally:
    print('resource closed')'''

###EXcpetion handling using user input:

'''a=int(input("Enter a number:  "))
b=int(input('Enter a number:  '))


try:
    
    print('resource open')
    print(a / b)
    s=int(input("Enter a Number:  "))
    print(s)

except ZeroDivisionError as e:
    print("Hey, you cannot divide a number by zero",e)

except ValueError as e:
    print("Invalid Input")

except Exception as e:
    print("Something went Wrong")

finally:
    print('resource closed')'''


'''a=int(input("Enter a number: "))
b=int(input("Enter a number: "))

try:
    print("Resource Open")
    print(a/b)
    s=int(input("Enter a number: "))
    print(s)

except ZeroDivisionError as e:
    print("hey you cannot divide a number by Zero",e)

except ValueError as e:
    print("Invalid Input")
    
finally:
    print("Resource close")'''
