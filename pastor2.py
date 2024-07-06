#!/usr/bin/env python
# coding: utf-8

# In[16]:


import pandas as pd
a1=pd.read_csv(r"D:\pastor\till500 correct.csv")
a2=pd.read_csv(r"D:\pastor\till618 correct.csv")
a3=pd.read_csv(r"D:\pastor\till999 correct.csv")
a4=pd.read_csv(r"D:\pastor\till1500 correct.csv")
a5=pd.read_csv(r"D:\pastor\till1582 correct.csv")
a1.columns=["ind","details"]
a2.columns=["ind","details"]
a3.columns=["ind","details"]
a4.columns=["ind","details"]
a5.columns=["ind","details"]
f1=pd.concat([a1,a2,a3,a4,a5],axis=0)
f1.drop("ind",axis="columns")
f1.to_csv(r"D:\pastor\finalop.csv")

