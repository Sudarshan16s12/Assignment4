#!/usr/bin/env python
# coding: utf-8

# In[2]:


#Write a Python program to create a lambda function that adds 25 to a given number passed in as an argument.
x=10
y = lambda x : x+25
print(y(x))


# In[1]:


#Write a Python program to triple all numbers of a given list of integers. Use Python map.
l1=[1,2,3,4,5,6,7]
result=(map(lambda n:n*3,l1))
print(list(result))


# In[4]:


#Write a Python program to square the elements of a list using map() function.
l2=[4,5,2,9]
result=(map(lambda n:n**2,l2))
print(list(result))


# In[ ]:




