#!/usr/bin/env python
# coding: utf-8

# In[1]:


from IPython.core.display import display, HTML
display(HTML("<style>.container { width:100% ! important; }<style>"))


# In[10]:


import nltk
nltk.download("punkt")


# In[19]:


print(" alex christopher Assignment")
print("")
t=input("sample text input : ")


# In[3]:


print("Sentence Tokenization using NLTK library")
print()
from nltk.tokenize import sent_tokenize
t1=sent_tokenize(t)
for x in t1:
    print("-> ",x)


# In[4]:


print("Word Tokenization using NLTK library")
print()
from nltk.tokenize import word_tokenize
t2=word_tokenize(t)
print(t2)


# In[5]:


print("Sentence Tokenization using string methods")
print()
t3=t.replace(".","\n")
t4=t3.splitlines()
for y in t4:
    print("-> ",y)
        


# In[6]:


print("Word tokenize using string methods")
print()
t5=t.split()
print(t5)


# In[7]:


from nltk.probability import FreqDist
fdist = FreqDist(t)
print(fdist.most_common())


# In[8]:


f=input("enter the character : ")
print(t.count(f))


# In[11]:


nltk.download("stopwords")


# In[12]:


from nltk.corpus import stopwords
stop_words=set(stopwords.words("english"))
print(stop_words)


# In[13]:


list1=[]
for o1 in t2:
    if o1 not in stop_words:
        list1.append(o1)
print(list1)


# In[14]:


puctio = [",",".","!","'"]
for o2 in t2:
    if o2 in puctio:
        t2.remove(o2)
print(t2)


# In[15]:


print(" ".join(t2))


# In[16]:


nltk.download("wordnet")


# In[18]:


from nltk.stem.wordnet import WordNetLemmatizer
from nltk.stem.porter import PorterStemmer
lem = WordNetLemmatizer()
stem = PorterStemmer()
word = "cricketer"
print("Lemmatized Word:",lem.lemmatize(word,"v"))
print("Stemmed Word:",stem.stem(word))

