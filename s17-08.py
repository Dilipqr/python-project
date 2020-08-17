# Abstract class:
# ABC classes are called----Abstract Base Classes
# Abstract class having one abstract method
# Abstract method means we will use future purpose we will write set of lines of code passes in the abstract method.
# Abstract class means the method inside the class is called abstract class.

from abc import ABC, abstractmethod

class Computer(ABC):  # subclass    #class    #ABC-abstract class
    @abstractmethod
    def process(self):  # methods
        pass  # print("running")    #Body can have multiple statements


class Laptop(Computer):
    def process(self):
        print("running")


class Programmer:
    def work(self, com):
        print("solving problems")
        com.process()


#objects of class
com1 = Laptop()
prog1 = Programmer()
prog1.work(com1)
com1.process()

'''class Sai(ABC):
    @abstractmethod
    def a(self):
        pass


class Ram(Sai):
    def a(self):
        print("ML")


class Dilip:
    def c(self, r1):
        print("python")
        r1.a()''


r1 = Ram()
d1 = Dilip()
d1.c(r1)
r1.a()'''

# Private        x=__10
# Public         x=10
# protected      x=_10

'''from abc import ABC
class Test(ABC):
    def __init__(self):
        self.var1 = 1
        self._var2 = 11
        self.__var3 = 39
        # print(self.__var3)
    # def sai(self):
    # print(self.__var3)


t = Test()
print(t.var1)'''

#Interfaces:

'''from abc import ABC,abstractmethod
class Sai(ABC):
    @abstractmethod
    def func1(self):
        pass

class Ram(Sai):
    def func1(self):
        print("ml")


r=Ram()
r.func1()'''


