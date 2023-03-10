#!/usr/bin/env python
# coding: utf-8

# In[1]:


#For Loop

"""
Syntax of For Loop is :-

for iterating_variable in sequence:
    print(iterating_variable)
    statements
"""


# In[6]:


list1 = [1,2,3,4,5,6,7,8,9]
for x in list1:
    print(x)


# In[9]:


# range() function:--
"""
Syntax of range():
range(begin  , end , step)

begin = 0 (by default)
end = end-1
step = -1 it is strating from last
"""
#l = [1,2,3,4,5,6,7,8,9]

print(list(range(5)))




# In[10]:


print(list(range(1,5)))


# In[14]:


print(list(range(1,10,2)))


# In[12]:


print(list(range(5,0,-1)))


# In[15]:


print(list(range(-4,4)))


# In[16]:


print(list(range(-4,4,2)))


# In[17]:


print(list(range(1,1)))


# In[18]:


print(list(range(0,1)))


# In[20]:


#Print the numbner from 1 to 10 using range function


for i in range(1,11):
    print(i , end=' ')


# In[8]:


#Program to print the prime numbers in between a range 


start = int(input("Enter the Starting number:"))
end = int(input("Enter the ending number:"))
for n in range(start , end+1):
    if(n>1):
        for i in range(2 ,n):
            if(n%i)==0:
                break
        else:
            print(n)
                
    


# In[12]:


#Program to find the whether my nos is prime or not

n= int(input("Enter a  number:"))
for i in range(2 ,n+1):
    if(n%i)==0:
        break
if i==n:
    print(n ," is a prime nos")
else:
    print(n , " is not a prime nos")
        
        


# In[13]:


#Loop Control Statements


for letter in 'Ahana':
    if letter == 'n':
        break
    print("Current letter" , letter)
    


# In[16]:


var = 10
while var>0:
    print("Current variable value :" ,var)
    var = var-1
    if var == 5:
        break
print("out of the loop")


# In[17]:


for letter in 'Ahana':
    if letter == 'n':
        continue
    print("Current letter" , letter)


# In[19]:


var = 5
while var >0:
    var = var-1
    if var == 3:
        continue
    print("Current Vraibale value" , var)
print("In  loop")

    


# In[20]:


for letter in 'Ahana':
    if letter == 'n':
        pass
    print("Current letter" , letter)


# In[2]:


#Nested For Loops:

"""
1
12
123
1234
"""

for i in range(1,10):
    for j in range(1 ,(i+1)):
        print(j,end=" ")
    print()


# In[1]:


i =1
while i<5:
    j = 1
    while j<(i+1):
        print(j , end=' ')
        j = j+1
       
    print()
    i= i+1
    


# In[8]:


for i in range(1,10):
    for j in range(1 ,(i-1)):
        print('$',end=" ")
    print()


# In[ ]:




