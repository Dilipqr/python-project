# oops concepts:
# class is blueprint from which specific objects are created:
# class  and objects:
'''class Car():
    pass

honda=Car()
swift=Car()

honda.modelname='city'
honda.price='900000'
honda.yearm=2012

swift.modelname='Dzire'
swift.price='600000'
swift.yearm=2016

print(swift.price)'''

# CONSTRUCTORS:
'''class Car():
    def __init__(self,modelname,price,yearm):
        self.modelname=modelname
        self.price=price
        self.yearm=yearm

honda=Car('city','9000000','2012')
swift=Car('Dzire','6000000','2016')

print(swift.price)'''

# Add Objects:
'''class Car():
    def __init__(self,modelname,price,yearm):
        self.modelname=modelname
        self.price=price
        self.yearm=yearm

honda=Car('city','9000000','2012')
swift=Car('Dzire','6000000','2016')

honda.cc=1200

print(honda.__dict__)'''

# UPDATE THE VALUE:
'''class Car():
    def __init__(self,modelname,price,yearm):
        self.modelname=modelname
        self.price=price
        self.yearm=yearm

    def price_inc(self):
        self.price=int(self.price*1.15)

honda=Car('city',9000000,'2012')
swift=Car('Dzire',6000000,'2016')

print(honda.price)
honda.price_inc()
print(honda.price)'''

# Inheritance:
# Basic Example
'''class Sai:

    def feature1(self):
        print("Feature 1 is working")

    def feature2(self):
        print("Feature 2 is working")

a1=Sai()
a1.feature1()
a1.feature2()'''

'''class Car():
    def __init__(self,modelname,price,yearm):
        self.modelname=modelname
        self.price=price
        self.yearm=yearm

    def price_inc(self):
        self.price=int(self.price*1.15)

class SaiCar(Car):
    pass

honda=saiCar('city',9000000,'2012')
swift=Car('Dzire',6000000,'2016')

print(honda.price)
honda.price_inc()
print(honda.price)'''

# help function:
'''class Car():
    def __init__(self,modelname,price,yearm):
        self.modelname=modelname
        self.price=price
        self.yearm=yearm

    def price_inc(self):
        self.price=int(self.price*1.15)

class SaiCar(Car):
    pass

honda=SaiCar('city',9000000,'2012')
swift=Car('Dzire',6000000,'2016')

print(help(honda))
honda.price_inc()
print(honda.price)'''

# super class:

'''class Car():
    def __init__(self,modelname,price,yearm):
        self.modelname=modelname
        self.price=price
        self.yearm=yearm
    def price_inc(self):
        self.price=int(self.price*1.15)

class SaiCar(Car):
    def __init__(self, modelname, price, yearm, cc):
        super().__init__(modelname, price, yearm)
        self.cc=cc

honda= SaiCar('city', 9000000, 2012,1200)
swift=Car('Dzire',6000000,2016)

honda.price_inc()
print(honda.price)'''

# SIngle level Inheritance
# Multi level    "
# Multiple Level  "
'''class Sai():

    def feature1(self):
        print("Feature 1 is working")

    def feature2(self):
        print("Feature 2 is working")

#a1=Sai()
#a1.feature1()
#a1.feature2()

class Ram(Sai):
    def feature3(self):
        print("Feature 3 is working")

    def feature4(self):
        print("Feature 4 is working")

#b1=Ram()
#b1.feature3()
#b1.feature4()


class Dilip(Ram):

    def feature5(self):
        print("Feature 5 is working")


c1 = C()

c1.feature1()
c1.feature2()
c1.feature3()
c1.feature4()
c1.feature5()'''


# Multiple level

class Sai():

    def feature1(self):
        print("Feature 1 is working")

    def feature2(self):
        print("Feature 2 is working")


# a1=Sai()
# a1.feature1()
# a1.feature2()

class Ram():
    def feature3(self):
        print("Feature 3 is working")

    def feature4(self):
        print("Feature 4 is working")


# b1=Ram()
# b1.feature3()
# b1.feature4()

class C(Sai, Ram):

    def feature5(self):
        print("Feature 5 is working")


c1 = C()

c1.feature1()
c1.feature2()
c1.feature3()
c1.feature4()
c1.feature5()

