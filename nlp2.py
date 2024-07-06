#!/usr/bin/env python
# coding: utf-8

# In[1]:


from IPython.core.display import display, HTML
display(HTML("<style>.container { width:100% ! important; }<style>"))


# In[1]:


pip install pyttsx3


# In[2]:


import pyttsx3
a=pyttsx3.init()
b="hey! say my name as Alex Christopher"
a.say(b)
a.runAndWait()


# In[11]:


import nltk


# In[17]:


from nltk.tokenize import word_tokenize
from nltk.tokenize import sent_tokenize
from sklearn.feature_extraction.text import CountVectorizer


# In[15]:


d=input()
dd=sent_tokenize(d)
print(dd)


# In[24]:


preprocessed_document=[''.join(word_tokenize(doc.lower())) for doc in dd]
vectorizer=CountVectorizer()
bow_matrix=vectorizer.fit_transform(preprocessed_document)
vocabulary=vectorizer.get_feature_names_out()
print("matrix :",bow_matrix.toarray())
print()
print("words present :",vocabulary)

