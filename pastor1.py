#!/usr/bin/env python
# coding: utf-8

# In[96]:


text=input("data : ")


# In[97]:


text


# In[ ]:


#original


# In[98]:


list1=[]
for x in range(2,10,1):
    a=". 00"
    b=str(x)
    c=a+b
    list1.append(c)
list1


# In[99]:


list2=[]
for x in range(10,100,1):
    a=". 0"
    b=str(x)
    c=a+b
    list2.append(c)


# In[100]:


list2m=[]
for x in range(100,501,1):
    a=". "
    b=str(x)
    c=a+b
    list2m.append(c)
print(list2m)


# In[101]:


for y in list2:
    list1.append(y)
print(list1)


# In[102]:


for y in list2m:
    list1.append(y)
print(list1)


# In[ ]:


#point 2 space


# In[103]:


list3=[]
for x in range(2,10,1):
    a=".  00"
    b=str(x)
    c=a+b
    list3.append(c)
print(list3)


# In[104]:


list4=[]
for x in range(10,100,1):
    a=".  0"
    b=str(x)
    c=a+b
    list4.append(c)


# In[105]:


list4m=[]
for x in range(100,501,1):
    a=".  "
    b=str(x)
    c=a+b
    list4m.append(c)
print(list4m)


# In[106]:


for y in list4:
    list3.append(y)
print(list3)


# In[107]:


for y in list4m:
    list3.append(y)
print(list3)


# In[ ]:


#no point 2 space


# In[108]:


list5=[]
for x in range(2,10,1):
    a="  00"
    b=str(x)
    c=a+b
    list5.append(c)
list5


# In[109]:


list6=[]
for x in range(1,100,1):
    a="  0"
    b=str(x)
    c=a+b
    list6.append(c)


# In[111]:


list6m=[]
for x in range(100,501,1):
    a="  "
    b=str(x)
    c=a+b
    list6m.append(c)
print(list6m)


# In[112]:


for y in list6:
    list5.append(y)
print(list5)


# In[113]:


for y in list6m:
    list5.append(y)
print(list5)


# In[ ]:


#point 3 spaces


# In[114]:


list7=[]
for x in range(2,10,1):
    a=".   00"
    b=str(x)
    c=a+b
    list7.append(c)
print(list7)


# In[115]:


list8=[]
for x in range(10,100,1):
    a=".   0"
    b=str(x)
    c=a+b
    list8.append(c)


# In[116]:


list8m=[]
for x in range(100,501,1):
    a=".   "
    b=str(x)
    c=a+b
    list8m.append(c)
print(list8m)


# In[117]:


for y in list8:
    list7.append(y)
print(list7)


# In[118]:


for y in list8m:
    list7.append(y)
print(list7)


# In[ ]:


#page generator


# In[119]:


qq=[]
for x in range(2,30,1):
    a="Page "
    b=str(x)
    c=" of 92"
    d=a+b+c
    qq.append(d)
print(qq)


# In[ ]:





# In[120]:


for x in range(0,499,1):
    text=text.replace(list3[x],list1[x])
for x in range(0,499,1):
    text=text.replace(list5[x],list1[x])
for x in range(0,499,1):
    text=text.replace(list1[x],"\n")
final=text.splitlines()
final


# In[123]:


import pandas as pd
dict1={"pastordetails":final}
gg=pd.DataFrame(dict1)
gg.to_csv(r"D:\pastor\till500.csv")

