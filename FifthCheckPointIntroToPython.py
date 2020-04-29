#!/usr/bin/env python
# coding: utf-8

# In[13]:


import numpy as np 
d = np.array([[2,3,4], [5,6,7], [1,2,3]])
print(d)
b = d.reshape(1, -1) 
print(b)


# In[20]:


# Write a NumPy program to compute the sum of the diagonal element of a given array.
import numpy as np 
d1 = np.arange(9).reshape(3,3)
d2 = np.array([[2,3,4], [5,6,7], [1,2,3]])
print(d1)
print(d2)
print(d1.trace()) # numpy.trace() is a function that return the sum along diagonals of the array.
print(d2.trace())


# In[ ]:


# Given an array of your choice, get all the values higher than X : if a = [[1,2],[3,5]] and x = 3 :  then 3 and 5 are higher than 2. 
# "Array is"+list+"and x = "+x+" "+
import numpy as np 
d = np.array([[1,2],[3,5]])
r=d.reshape(1,-1)
x=3
count=0
s=""
for j in range(r[0,-1]):
        if r[0,j] >= x: 
            s=s+str(r[i,j])
            count+=1
s="then"
print("a = "+str(d)+" and x = "+str(x)+s+" are higher than "+str(count))


# In[93]:


# Given two arrays A&B having the same shape.  The task is to apply addition by hand : C is the new array. 
import numpy as np
A = np.array([1,2,3,4])
B = np.array([1,2,3,4])
C = A + B
print(C)


# In[94]:


# Write a NumPy program to subtract the mean of each row of a given matrix.
import numpy as np
array = np.array([[2, 5], [7, 9]])
print("Mean of each column")
print(array.mean(axis=0))
print("Mean of each row")
print(array.mean(axis=1))

