#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# In[2]:


print (dir(np))


# In[3]:


np.dot ([3,4],[4,15])


# In[4]:


np.sqrt(10)


# In[5]:


np.min([12,34,233,22423])


# In[7]:


print('minimum',np.min([12,34,233,22423]))


# In[8]:


np.ceil(29.44)


# In[9]:


np.ceil(np.sqrt(10))


# In[10]:


help(np)


# In[11]:


xyz = np.array([5,9,23])


# In[12]:


print (xyz)


# In[13]:


type(xyz)


# In[14]:


b=np.asarray(xyz)
print(b)


# In[17]:


np.array([2,4,3,3], dtype=float)


# In[19]:


my_mat = [[1,2,3],[2,4,3],[3,4,5]]

mat = np.array(my_mat)

print("Type/class of this object:",type(mat))

print("Here is the matrix\n________\n",mat,"\n_________")

print('Dimension of the matrix:', mat.ndim)

print('Size of the matrix:', mat.size)

print ('Shape of the matrix:', mat.shape)

print ('Data type of the matrix:', mat.dtype)


# In[14]:


a= (2,10.5,.4)
a =np.arange(2,10.5,.4)
a


# In[15]:


a[::-1]


# In[13]:


print("Every 5th number from 50 in reverse order\n",np.arange(50,-1,-5))


# In[16]:


list(range(2,10.5,.4))


# In[17]:


print("Linearly spaced numbers between 10 and 40\n-------------" )
print(np.linspace(10,40,5))


# In[11]:





# In[2]:


print('Vector of zeroes\n_____')

print(np.zeros(5))


# In[4]:


print('Matrix of zeroes\n_____')

print(np.zeros((5,6)))


# In[5]:


print('Matrix of ones\n_____')

print(np.ones((5,8)))


# In[9]:


print('Matrix of ones\n_____')

print(25*np.ones((5,8)))


# In[10]:


x = np.arange(30).reshape(6,5)
print(x)


# In[11]:


np.random.seed(7)

print(np.random.rand(5,6))
    


# In[3]:


print('Number from normal distribution with zero mean and standard deviation 1 i.e. standard normal')

print (np.random.randn(10,3))


# In[5]:


print('random integer vector:',np.random.randint(5,23,10))


# In[6]:


print('Random integer matrix')
print(np.random.randint(1,2000,(6,7)))


# In[4]:


while True:
    otp1 = np.random.randint(1000,10000,1)
    print('Your otp is - ', otp1)
    user_otp = int(input('Enter your otp'))
    if otp1 == user_otp:
        print('LOgin Successful')
        break
    else:
        print('Invalid OTP,Generate new otp')
        continue


# In[2]:


from numpy.random import randint as ri


# In[13]:


M = ri(1,100,25).reshape(5,5)
print('Matrix of random integers\n','-'*50,'\n',M)
print('Here is the sorted matrix along each row\n','-'*50,'\n',np.sort(M))
print('Here is the sorted matrix along each column\n','-'*50,'\n',np.sort(M, axis=0))


# In[14]:


print ('Minimum = ', M.min(), 'and Maximum = ', M.max())


# In[15]:


emp_salary = ri(8,70,10)
emp_salary


# In[16]:


print(np.where(emp_salary < 25))


# In[17]:


emp_salary[np.where(emp_salary < 25)]


# In[18]:


np.clip(emp_salary, a_min=20, a_max=50)


# In[19]:


arr = np.arange(13,30)
print('Array:',arr)


# In[20]:


print('7th index is:',arr[7])


# In[22]:


print('7th, 4th and 9th index are:', arr[[7,4,9]])


# In[3]:


my_matrix = [[2,3,4],[4,5,6],[5,6,7]]
mat = np.array(my_matrix)
mat


# In[4]:


print('Element in row index 1 and column index 2:', mat[1][2])


# In[5]:


mat


# In[8]:


print('Entire row at index 2:', mat[2])
print('entire column at index:',mat[:,1:])


# In[10]:


print('\nentire column at index:\n',mat[:,1:])


# In[13]:


print('matrix with row indices 1 and 2 and column indices 3 and 4\n', mat[1:2,1:2])


# In[14]:


mat


# In[16]:


print('matrix with the given index\n', mat[0:2,[1,2]])


# In[17]:


print('matrix of the given index\n', mat[1:,1:2])


# In[19]:


print(mat[1:2,[0,2]])


# In[20]:


mat


# In[21]:


mat[0,1] = 23
print(mat)


# In[6]:


mat = np.array(ri(10,100,15)).reshape(3,5)
print('Matrix of two digit no\n-----------\n',mat)


# In[7]:


mat>50


# In[8]:


print('Elements greater than 50\n', mat[mat>50])


# In[9]:


marks = 70
np.where(marks>68, 'pass','fail')


# In[11]:


non_zero = ri(-10,50,100)
print(non_zero)
np.count_nonzero(non_zero)


# In[3]:


flat = ri(2,20, size=(3,4))
print(flat)

flat.ravel()


# In[4]:


flat.flatten()


# In[10]:


mat1 = np.array(ri(1,10,9)).reshape(3,3)
mat2 = np.array(ri(1,10,9)).reshape(3,3)

print('\n1st matrix\n', mat1)
print('\n2nd matrix\n-----------\n', mat2)


# In[13]:


print('\naddition of both matrix\n---------\n',mat1+mat2)


# In[14]:


mat3 = np.array(ri(1,10,9)).reshape(3,3)
print(mat3)


# In[16]:


rows = np.array([[1,0,2]])
print(rows)


# In[18]:


y = mat3 + rows
print(y)


# In[19]:


new_rows = rows.T
print(new_rows)


# In[20]:


x = mat3 + new_rows
print(x)


# In[ ]:




