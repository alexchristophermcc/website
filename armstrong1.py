#!/usr/bin/env python
# coding: utf-8

# In[1]:


a=int(input("enter a number: "))
b=str(a)
list1=[]
list2=[]
for x in b:
    list1.append(int(x))
c=len(list1)
for x in list1:
    d=x**c
    list2.append(d)
final=sum(list2)
if final == a:
    print("this is a armstrong number")
else:
    print("this is not a armstrong number")

