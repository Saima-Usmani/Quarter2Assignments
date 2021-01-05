#!/usr/bin/env python
# coding: utf-8

# # Numpy_Assignment_2::

# ## Question:1

# ### Convert a 1D array to a 2D array with 2 rows?

# #### Desired output::

# array([[0, 1, 2, 3, 4],
#         [5, 6, 7, 8, 9]])

# In[2]:


import numpy as np
np.arange(10).reshape(2,5)


# ## Question:2

# ###  How to stack two arrays vertically?

# #### Desired Output::
array([[0, 1, 2, 3, 4],
        [5, 6, 7, 8, 9],
       [1, 1, 1, 1, 1],
       [1, 1, 1, 1, 1]])
# In[4]:


f=np.array([[0, 1, 2, 3, 4],[5, 6, 7, 8, 9]])
g=np.array([[1, 1, 1, 1, 1],[1, 1, 1, 1, 1]])
np.vstack((f,g))


# ## Question:3

# ### How to stack two arrays horizontally?

# #### Desired Output::
array([[0, 1, 2, 3, 4, 1, 1, 1, 1, 1],
       [5, 6, 7, 8, 9, 1, 1, 1, 1, 1]])
# In[5]:


np.hstack((f,g))


# ## Question:4

# ### How to convert an array of arrays into a flat 1d array?

# #### Desired Output::
array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
# In[ ]:


f=np.array([[0, 1, 2, 3, 4],[5, 6, 7, 8, 9]])
f.flatten()


# ## Question:5

# ### How to Convert higher dimension into one dimension?

# #### Desired Output::
array([ 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14])
# In[6]:


higherd=np.arange(15).reshape(3,5)
higherd.flatten()


# ## Question:6

# ### Convert one dimension to higher dimension?

# #### Desired Output::
array([[ 0, 1, 2],
[ 3, 4, 5],
[ 6, 7, 8],
[ 9, 10, 11],
[12, 13, 14]])
# In[8]:


ar=np.arange(15).reshape(5,3)
ar


# ## Question:7

# ### Create 5x5 an array and find the square of an array?

# In[9]:


aa=np.arange(25).reshape(5,5)
aa ** 2


# ## Question:8

# ### Create 5x6 an array and find the mean?

# In[10]:


arr=np.arange(30).reshape(5,6)
arr.mean()


# ## Question:9

# ### Find the standard deviation of the previous array in Q8?

# In[11]:


np.std(arr)


# ## Question:10

# ### Find the median of the previous array in Q8?

# In[12]:


np.median(arr)


# ## Question:11

# ### Find the transpose of the previous array in Q8?

# In[ ]:


arr.T


# ## Question:12

# ### Create a 4x4 an array and find the sum of diagonal elements?

# In[13]:


ar4d=np.arange(16).reshape(4,4)
sumofd=sum(np.diagonal(ar4d))
sumofd


# ## Question:13

# ### Find the determinant of the previous array in Q12?

# In[ ]:


np.linalg.det(ar4d)


# ## Question:14

# ### Find the 5th and 95th percentile of an array?

# In[14]:


ar1 = [20, 2, 7, 1, 34]
np.percentile(ar1, 5)
np.percentile(ar1, 95)


# ## Question:15

# ### How to find if a given array has any null values?

# In[17]:


arname = np.array([-1, 0, 1, 2, 3, -5, 0.3])
np.isnan(arname)


# In[ ]:




