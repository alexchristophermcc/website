#!/usr/bin/env python
# coding: utf-8

# In[1]:


from IPython.core.display import display, HTML
display(HTML("<style>.container { width:100% ! important; }<style>"))


# In[2]:


import pandas as pd
alex1=pd.read_csv(r"C:\Users\Admin\Desktop\gifta\OTT PLATFORM SURVEY (Responses) - Form Responses 1.csv")
alex1


# In[3]:


alex2=alex1.dropna()
alex2.info()


# In[4]:


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


# In[5]:


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


# In[6]:


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


# In[7]:


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


# In[8]:


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


# In[10]:


dummy1=pd.DataFrame(dict1)
dummy2=pd.DataFrame(dict2)
dummy3=pd.DataFrame(dict3)
dummy4=pd.DataFrame(dict4)
dummy5=pd.DataFrame(dict5)
dummy6=pd.concat([dummy1,dummy2,dummy3,dummy4,dummy5],axis=1)
dummy6.to_csv(r"D:\check.csv")


# In[10]:


dummy7=alex2["WHICH OTT PLATFORM YOU GENERALLY PREFER WHEN YOUR BORED?"]
dummy7


# In[18]:


from sklearn.tree import DecisionTreeClassifier
from sklearn import svm
from sklearn.metrics import accuracy_score as dum
model1=svm.SVC()
model1.fit(dummy6,dummy7)


# In[20]:


print("uesful -> 1\nmoderate -> 2\ncan't relate -> 3")
op1=[]
op2=[]
for xx in alex2["WHICH OTT PLATFORM YOU GENERALLY PREFER WHEN YOUR BORED?"]:
    if xx not in op1:
        op1.append(xx)
print("\n\n")
for yy in op1:
    print(yy)
    inbut=int(input("tell me your opinion on above OTT platform :"))
    if inbut == 1 or inbut == 2 or inbut == 3:
        op2.append(inbut)
    else:
        print("you have entered a wrong digit")
final=model1.predict([op2])
print("\n\n")
for zz in final:
    print("based on the opinions you gave to me, i prefer you to use",zz,". have a nice day :)")

