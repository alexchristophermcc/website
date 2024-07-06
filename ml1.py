#!/usr/bin/env python
# coding: utf-8

# In[1]:


from IPython.core.display import display, HTML
display(HTML("<style>.container { width:100% ! important; }<style>"))


# In[3]:


import pandas as pd
alex1=pd.read_csv(r"C:\Users\Admin\Desktop\gifta\OTT PLATFORM SURVEY (Responses) - Form Responses 1.csv")
alex1


# In[4]:


alex2=alex1.dropna()
alex2.info()


# In[5]:


list1=[]
for x1 in alex2["OPINION [netflix]"]:
    if x1=="useful":
        list1.append(1)
    elif x1=="moderate":
        list1.append(2)
    else:
        list1.append(3)
print("1-> Useful\n2-> Moderate\n3-> Can't relate")
dict1={"netflix":list1}
print(dict1)


# In[24]:


list2=[]
for x2 in alex2["OPINION [amazon prime]"]:
    if x2=="useful":
        list2.append(1)
    elif x2=="moderate":
        list2.append(2)
    else:
        list2.append(3)
print("1-> Useful\n2-> Moderate\n3-> Can't relate")
dict2={"amazon prime":list2}
print(dict2)


# In[25]:


list3=[]
for x3 in alex2["OPINION [disney hotstar]"]:
    if x3=="useful":
        list3.append(1)
    elif x3=="moderate":
        list3.append(2)
    else:
        list3.append(3)
print("1-> Useful\n2-> Moderate\n3-> Can't relate")
dict3={"disney hotstar":list3}
print(dict3)


# In[26]:


list4=[]
for x4 in alex2["OPINION [jio cinema]"]:
    if x4=="useful":
        list4.append(1)
    elif x4=="moderate":
        list4.append(2)
    else:
        list4.append(3)
print("1-> Useful\n2-> Moderate\n3-> Can't relate")
dict4={"jio cinema":list4}
print(dict4)


# In[27]:


list5=[]
for x5 in alex2["OPINION [zee 5]"]:
    if x5=="useful":
        list5.append(1)
    elif x5=="moderate":
        list5.append(2)
    else:
        list5.append(3)
print("1-> Useful\n2-> Moderate\n3-> Can't relate")
dict5={"zee 5":list5}
print(dict5)


# In[28]:


dummy1=pd.DataFrame(dict1)
dummy2=pd.DataFrame(dict2)
dummy3=pd.DataFrame(dict3)
dummy4=pd.DataFrame(dict4)
dummy5=pd.DataFrame(dict5)
dummy6=pd.concat([dummy1,dummy2,dummy3,dummy4,dummy5],axis=1)
dummy6


# In[48]:


dummy7=alex2["WHICH OTT PLATFORM YOU GENERALLY PREFER WHEN YOUR BORED?"]
dummy7


# In[57]:


from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
a,b,c,d=train_test_split(dummy6,dummy7,test_size=0.3,random_state=1)

from sklearn.tree import DecisionTreeClassifier
model1=DecisionTreeClassifier()
model1.fit(a,c)
pred1=model1.predict(b)
print(dum(d,pred1))


# In[35]:


from sklearn.naive_bayes import GaussianNB
model2=GaussianNB()
model2.fit(a,c)
pred2=model2.predict(b)
print(dum(d,pred2))


# In[36]:


from sklearn.linear_model import LogisticRegression
model3=LogisticRegression()
model3.fit(a,c)
pred3=model3.predict(b)
print(dum(d,pred3))


# In[37]:


from sklearn.neighbors import KNeighborsClassifier
model4=KNeighborsClassifier()
model4.fit(a,c)
pred4=model4.predict(b)
print(dum(d,pred4))


# In[58]:


from sklearn import svm
model5=svm.SVC()
model5.fit(a,c)
pred5=model5.predict(b)
print(dum(d,pred5))


# In[39]:


from sklearn.ensemble import RandomForestClassifier
model6=RandomForestClassifier()
model6.fit(a,c)
pred6=model6.predict(b)
print(dum(d,pred6))


# In[ ]:




