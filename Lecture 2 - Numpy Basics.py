#!/usr/bin/env python
# coding: utf-8

# # Lecture 2 - Numpy basics
# 
# ## 1. Numpy array definitions
# 
# * The number of dimensions is the **rank** of the array; 
# * The **shape** of an array is a tuple of integers giving the size of the array along each dimension

# In[6]:


import numpy as np

a = np.array([1, 2, 3])   #Here we create a rank 1 numpy array
print(f'1. The type of variable a is {type(a)}')        
print(f'2. The shape of variable a is {a.shape}')       
print(f'3. The rank of a is {a.ndim}')

b = np.array([[1, 2, 3],[4, 5, 6]])  #Here we create a rank 2 numpy array
print(f'4. The shape of variable b is {b.shape}')       
print(f'5. The rank of b is {b.ndim}')

c = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]]) #Here we create a rank 3 numpy array
print(f'6. The shape of variable c is {c.shape}') 
print(f'7. The rank of c is {c.ndim}')

# You can reshape your array dimensions using the reshape function
d = b.reshape(3, 2)
print(f'8. The original array is: {b}')
print(f'9. The reshaped array is: {d}')


# In[21]:


import numpy as np
c = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]]) #Here we create a rank 3 numpy array
print(c)
print(f'6. The shape of variable c is {c.shape}') 
print(f'7. The rank of c is {c.ndim}')


# ## 2. Numpy array indexing
# 
# Positions in numpy arrays can be accessed or modified using nonnegative integers. 

# In[90]:


print('Elements can be accessed by their positions starting with 0')
print(f'1. a = {a}')
print(f'2. a[0] = {a[0]}, a[1] = {a[1]}, a[2] = {a[2]}')  

print('Changes in the values are also done by the position index.')
a[0] = 5 # Change an element of the array
print(f'3. after changing a[0], a = {a}')         

# The same idea works for a 2Dimensional numpy array
print(f'b = {b}')
print(f'4. b[0, 0] = {b[0, 0]}, b[0, 1] = {b[0, 1]}, b[1, 0] = {b[1, 0]}') 


# In[3]:


a = np.array([1, 2, 3])
 
print(b)
print(b[1,1])


# ## 3. Numpy array creation functions
# 
# ### arange
# This function creates an array within a range with regularly incrementing values. 
# 
# ### linspace 
# This function will create arrays with a specified number of elements, and spaced equally between the specified beginning and end values.

# In[9]:


print('arange examples')
a = np.arange(10) #if one argument is passed it will be considered as the stop value
print(f'a = {a}')
b = np.arange(2, 10, dtype=float) #with two arguments, the first is the start value and the second is the stop val
print(f'b = {b}')
c = np.arange(2, 3, 0.1) #if a third parameter is passed, the value will be used as the increment
print(f'c = {c}')

print('linspace examples')
d = np.linspace(0, 9, 50) #the third is the number of elements to be created, including stop position
print(f'd = {d}')
e = np.linspace(1., 4., 7) 
print(f'e = {e}')


# In[13]:


a=np.linspace(5, 9, 4) 
print(a)


# The following creation functions define arrays based on the desired shape. 
# These functions can create arrays with any dimension by specifying how many dimensions and length along that dimension in a tuple or list.
# 
# ### zeros
# 
# Creates an array with the desired shape with all elements equal to 0.
# 
# ### ones 
# 
# Creates an array with the desired shape with all elements equal to 1.
# 
# ### full 
# 
# Creates an array with the desired shape with all elements equal to a specified value.
# 
# ### random 
# 
# Creates an array with the desired shape with all elements with random numbers.

# In[81]:


a = np.zeros((2, 2))   
print(f'a = {a}')
                      
b = np.ones((5, ))    
print(f'b = {b}')     

c = np.full((3, 2), 7)  
print(f'c = {c}')              
                       
d = np.random.random((2, 3))  
print(f'd = {d}')                                                  


# In[13]:


a= np.random.random((1))
print(f'a={a}')


# ## 4. Numpy array slicing
# 
# The most common way for slicing a numpy array is to provide parameters separated by a colon **:** (start:stop:step) directly to the ndarray object.

# In[65]:


a = np.arange(9) 
a = a.reshape(3,3)
print(a[:2])
print(f'1. The initial array is {a}')
print(f'2. The sliced array is {a[2:7:2]}') #start:stop:step example
print(f'3. The sliced array is {a[2:8]}') #start:stop example, with no step, so all values are included
a = a.reshape(3,3)
print(f'4. The initial array is {a}')      
print(f'5. a[1:2] = {a[1:2]}')  # gets second row only
print(f'6. a[1:] = {a[1:]}')   # gets from second row to the end
print(f'7. a[:1] = {a[:1]}')   # gets the first row only
print(f'8. a[:2] = {a[:2]}')   # gets the first row to row 2
print(f'9. a[:,0] = {a[:,0]}')  # gets the first column
print(f'10. a[:,-1] = {a[:,-1]}')# gets the last column
print(f'11. a[:,-2] = {a[:,-2]}')# gets the second last column

# we can use Boolean slicing to select elements of a numpy array.
# we will discuss this concept more in-depth in the next lecture
print(f'12. a[a > 2] = {a[a > 2]}') #
print(f'13. a[a < 6] = {a[a < 6]}') #


# In[68]:





# In[76]:


a=np.arange(49).reshape(7,7)
print(a[1:7:3,2:8:2])


# ## 5. Broadcasting 
# 
# The term broadcasting describes how NumPy treats arrays with different shapes during arithmetic operations. Subject to certain constraints, the smaller array is “broadcast” across the larger array so that they have compatible shapes. 
# Broadcasting provides a means of vectorizing array operations so that looping occurs in C instead of Python. 
# 
# NumPy operations are usually done on pairs of arrays on an element-by-element basis. 
# In the simplest case, the two arrays must have exactly the same shape, as in the following example.

# In[71]:


a = np.array([1.0, 2.0, 3.0])
b = np.array([5.0, 7.0, 10.0])

print(f'1. The result of a + b is {a + b}')
print(f'2. The result of b - a is {b - a}')
print(f'3. The result of a * b is {a * b}')
print(f'4. The result of b / a is {b / a}')


# NumPy’s broadcasting rule relaxes this constraint when the arrays’ shapes meet certain constraints. 
# The simplest broadcasting example occurs when an array and a scalar value are combined in an operation

# In[73]:


a = np.array([1.0, 3.0, 7.0])
b = 5.
print(f'1. The result of a + b is {a + b}')
print(f'2. The result of b - a is {b - a}')
print(f'3. The result of a * b is {a * b}')
print(f'4. The result of b / a is {b / a}')


# ## General Broadcasting Rules
# 
# When operating on two arrays, NumPy compares their shapes element-wise. It starts with the trailing (i.e. rightmost) dimensions and works its way left. Two dimensions are compatible when
# 
# * they are equal, or
# 
# * one of them is 1
# 
# If these conditions are not met, a **ValueError: operands could not be broadcast together** exception is thrown, indicating that the arrays have incompatible shapes. 
# 
# The **size of the resulting array is the size that is not 1 along each axis** of the inputs.

# In[67]:


a = np.array([[ 0.0,  0.0,  0.0],
           [10.0, 10.0, 10.0],
           [20.0, 20.0, 20.0],
           [30.0, 30.0, 30.0]])
b = np.array([1.0, 2.0, 3.0])
print(f'a + b = {a + b}')
b = np.array([1.0])


print(f'a + b = {a + b}')


# In[52]:


a=np.array([1,
           2])
print(a)

