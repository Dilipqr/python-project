# Polymorphism
# Operator Overloading
# 5+6   5,6 are operands,  and (+) are operator
# Synthetic Sugar means it is trying to simplify the code to the user

# Example1:

a = 9

b = 'world'

print(a + b)  # O/p: The output will be error: Unsupported operand type we can not use (+) Symbol

# Example2:

a = 4

b = 5

print(int.__add__(a, b))  # We use this method to add the ntwo numbers

a = 'Hello'

b = 'world'

print(str.__add__(a, b))  # We use this method two combinew string'''

# Magic methods:
# __add__
# __sub__
# __mul__

class Student:

    def __init__(self, marks1, marks2):
        self.marks1 = marks1
        self.marks2 = marks2

    def __add__(self, other):  # self=s1,other=s2
        marks1 = self.marks1 + other.marks1
        marks2 = self.marks2 + other.marks2
        s3 = Student(marks1, marks2)
        return s3


s1 = Student(45, 34)
s2 = Student(53, 49)

s3 = s1 + s2

print(s3.marks1)
print(s3.marks2)


# Comparing students marks:

class Student:

    def __init__(self, marks1, marks2):
        self.marks1 = marks1
        self.marks2 = marks2

    def __add__(self, other):  # self=s1,other=s2
        marks1 = self.marks1 + other.marks1
        marks2 = self.marks2 + other.marks2
        s3 = Student(marks1, marks2)
        return s3

    def __gt__(self, other):
        s1 = self.marks1 + self.marks2
        s2 = other.marks1 + other.marks2
        if s1 > s2:
            return True
        else:
            return False

s1 = Student(45, 34)
s2 = Student(53, 49)

s3 = s1 + s2

if s1 > s2:
    print("s1 Wins")
else:
    print("s2 Wins")


#Over Riding:

class Student:

    def __init__(self, marks1, marks2):
        self.marks1 = marks1
        self.marks2 = marks2

    def __add__(self, other):  # self=s1,other=s2
        marks1 = self.marks1 + other.marks1
        marks2 = self.marks2 + other.marks2
        s3 = Student(marks1, marks2)
        return s3

    def __gt__(self, other):
        s1 = self.marks1 + self.marks2
        s2 = other.marks1 + other.marks2
        if s1 > s2:
            return True
        else:
            return False

    def __str__(self):
        return ' {} {} '.format(self.marks1,self.marks2)

s1 = Student(45, 34)
s2 = Student(53, 49)

s3 = s1 + s2

if s1 > s2:
    print("s1 Wins")
else:
    print("s2 Wins")


print(s1)
print(s2)