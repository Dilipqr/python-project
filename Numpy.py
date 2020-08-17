#Numpy:
#Module or libreary used for python computing.
#It provides a high performance multidimensional array object and waiting with the arrays

'''import numpy as np
s=np.array([1,2,3])
print(s)'''
from numpy.core._multiarray_umath import ndarray

'''import numpy as np
s=np.array([(1,2,3),(4,5,6)])
print(s)'''

#Numpy (vs) List:
#occupies less memory
#Fast
#Conveninent with work numpy.
#Simple example for checking space b/w numpy and list

'''import numpy as np
import time
import sys
s=range(1000)
print(sys.getsizeof(5)*len(s)) #sys.getsize of(5) we will get the memory accupies by one element:
D=np.arange(1000)
print(D.size*D.itemsize)#D.size:space occuiped by one element      #D.itemsize:Space occuiped by the total item'''

#Fast:
'''import numpy as np
import time
import sys
size=1000000
l1=range(size)
l2=range(size)
a1=np.arange(size)
a2=np.arange(size)
start=time.time()
sai=[(x,y) for x,y in zip(4,(2))]
print((time.time()-start)*1000)
start=time.time()
sai=a1+a2
print(print((time.time()-start)*1000))'''

#Numpy operations:
#two dimensional:

'''import numpy as np
s=np.array([(1,2,3),(4,5,6)])
print(s.ndim)

#one dimensional:
import numpy as np
s=np.array([1,2,3])
print(s.ndim)

s=np.array([1,2,3])
print(s.itemsize)

s=np.array(9)
print(s.dtype)'''

#Size of array:
#Shape of array:

'''s=np.array([1,2,3,4,5,6,7,8,9])
print(s.size)

s=np.array([1,2,3,4,5,6,7,8,9])
print(s.shape)

s=np.array([(1,2,3,4,5,6,7,8,9),(1,2,3,4,5,6,7,8,9)])   #2rows, 9columns
print(s.shape)

#Reshape: change rows into columns and columns into rows:
import numpy as np
s=np.array([(1,2,3,4),(5,6,7,8)])
print(s.reshape(4,2))'''

#slicing:
'''import numpy as np
s=np.array([(1,2,3,4),(5,6,7,8)])
print(s[0:,3])

s=np.array([(1,2,3,4),(5,6,7,8),(6,7,8,9)])
print(s[0:,1])

r=np.array([(1,2,3,4),(5,6,7,8),(6,7,8,9)])
print(r[0:2,3])   # o/p:[4 8]

s=np.linspace(1,3,5)
print(s)
o/p: [1.  1.5  2.  2.5  3.]'''

#Min
#Max
#sum
'''import numpy as np
a=np.array([1,2,3])
print(a.min())
print(a.sum())
print(a.max())'''

#axis:
'''import numpy as np
s=np.array([(1,2,3),(4,5,6)])
print(s.sum(axis=0)) #[5 7 9]
s=np.array([(1,2,3),(4,5,6)])
print(s.sum(axis=1))'''

#SqureRoot:
'''import numpy as np
a=np.array([(1,2,3),(4,5,6)])
print(np.sqrt(a))

#Standard Deviation:
a=np.array([(1,2,3),(4,5,6)])
print(np.std(a))'''

#mathematical func:
'''import numpy as np
s=np.array([(1,2,3),(4,5,6)])
r=np.array([(1,2,3),(4,5,6)])
print(s+r)   #In list (+) is used for concatenation and numpy (+) is used for sum 
print(s-r)
print(s*r)
print(s/r)
print(s%r)
print(s^r)'''

#Ravel:
'''import numpy as np
s=np.array([(1,2,3),(4,5,6)])
print(np.ravel(s))  #[1 2 3 4 5 6]'''

#Vertial
#horizontal
'''import numpy as np
s=np.array([(1,2,3),(4,5,6)])
r=np.array([(1,2,3),(4,5,6)])
print(np.vstack((s,r)))
print(np.hstack((s,r)))

#s=np.array([(1,2,3),(4,5,6)])
#print(np.hstack(s))'''

#Numpy Special Functions:
#sine:
'''import numpy as np
import matplotlib.pyplot as plt
x=np.arange(0,4*np.pi,0.1)
y=np.sin(x)
plt.plot(x,y)
plt.show()'''

#cosine:
'''import numpy as np
import matplotlib.pyplot as plt
x=np.arange(0,4*np.pi,0.1)
y=np.cos(x)
plt.plot(x,y)
plt.show()'''