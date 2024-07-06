#!/usr/bin/env python
# coding: utf-8

# In[1]:


from IPython.core.display import display, HTML
display(HTML("<style>.container { width:100% ! important; }<style>"))


# In[7]:


import pandas as pd
a1=pd.read_csv(r"C:\Users\Admin\Desktop\data1.csv")
a1


# In[8]:


a2=a1.drop("Submitted Time",axis="columns")
a2


# In[9]:


a22=a2.isnull()
a22


# In[10]:


a3=a1.dropna()
a3


# In[11]:


list1=[]
list2=[]
for x in a1["7. How far is your favorite place from your home?"]:
    list1.append(x)
for y in list1:
    if "km" in y:
        s=y.replace("km","")
        t=int(s)
        list2.append(t)
print(list2)


# In[ ]:





# In[12]:


list3=[]
list4=[]
for z in a1["6. How often do you visit your favorite place?"]:
    list3.append(z)
for w in list3:
    if "(others)" not in w:
        list4.append(w)
print(list4)


# In[13]:


list5=[]
g,gg,ggg=0,0,0
for x in list2:
    if x>1 and x<100 :
        g=g+1
    elif x>100 and x<500 :
        gg=gg+1
    else:
        ggg=ggg+1
list5.append(g)
list5.append(gg)
list5.append(ggg)
print(list5)


# In[ ]:





# In[15]:


import matplotlib.pyplot as plt

plt.pie(list5,labels=["below 100 km","below 500 km","above 500 km"],explode=[0,0.1,0])
plt.title("favorite place's distance from their home                 ")
plt.legend()
plt.show()


# In[16]:


plt.hist(list4,edgecolor='black')
plt.title("visitation of their favorite place")
plt.ylabel("people")
plt.legend(["people"])
plt.show()


# In[17]:


x1=a3["10. Rate your favorite place"]
x2=a3["3. What is your favorite place?"]
plt.scatter(x1,x2,marker="s",s=100,color="green")
plt.xlabel("favorite place ratings")
plt.show()


# In[18]:


import statistics as sdd
liste=[]
for x in a3["10. Rate your favorite place"]:
    liste.append(x)
print(sdd.mean(liste))

