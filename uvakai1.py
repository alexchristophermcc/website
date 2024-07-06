#!/usr/bin/env python
# coding: utf-8

# In[1]:


from IPython.core.display import display, HTML
display(HTML("<style>.container { width:100% ! important; }<style>"))


# In[2]:


#location generator of xlsx
import pandas as pd
a=r"D:\uvakai\Lakes verified\L"
b=r"D:\uvakai\Lakes verified\C"
lakez=[]
for x in range(1,195,1):
    y=str(x)
    z=a+y+".xlsx"
    lakez.append(z)
print(lakez)


# In[3]:


#location generator of csv
alexz=[]
for x in range(1,195,1):
    y=str(x)
    z=b+y+".csv"
    alexz.append(z)
print(alexz)


# In[4]:


#converting xlsx to csv
for x in range(0,len(lakez),1):
    dummy1=pd.read_excel(lakez[x])
    dummy2=dummy1.to_csv(alexz[x],index=False)


# In[5]:


#assigning each csvdf to each variable
for i in range(1,195,1):
    globals()[f'storage{i}'] = pd.read_csv(alexz[i-1]) 


# In[6]:


for i in range(1,195,1):
    globals()[f'storage{i}'].columns=["aa","wsa","capacity"]


# In[8]:


for i in range(1,195,1):
    globals()[f'duplicateremoved{i}'] = globals()[f'storage{i}'].drop_duplicates(subset=["aa"])
duplicateremoved45


# In[11]:


davislake=pd.read_csv(r"D:\uvakai\Lakes\clakes.csv")
#merging with davis date and each lake
for i in range(1,195,1):
    globals()[f'merged{i}'] = pd.merge(davislake,globals()[f'duplicateremoved{i}'],on="aa",how="outer")
merged45


# In[12]:


qq=[]
for i in range(1,195,1):
    qp=len(globals()[f'merged{i}'])
    qq.append(qp)
print(qq)


# In[13]:


#variable name generator
w1=[]
for x in range(1,195,1):
    a=str(x)
    b="merged"+a
    w1.append(b)
sd=','.join(w1)
sd


# In[14]:


#final operation
yabba=pd.concat([merged1,merged2,merged3,merged4,merged5,merged6,merged7,merged8,merged9,merged10,merged11,merged12,merged13,merged14,merged15,merged16,merged17,merged18,merged19,merged20,merged21,merged22,merged23,merged24,merged25,merged26,merged27,merged28,merged29,merged30,merged31,merged32,merged33,merged34,merged35,merged36,merged37,merged38,merged39,merged40,merged41,merged42,merged43,merged44,merged45,merged46,merged47,merged48,merged49,merged50,merged51,merged52,merged53,merged54,merged55,merged56,merged57,merged58,merged59,merged60,merged61,merged62,merged63,merged64,merged65,merged66,merged67,merged68,merged69,merged70,merged71,merged72,merged73,merged74,merged75,merged76,merged77,merged78,merged79,merged80,merged81,merged82,merged83,merged84,merged85,merged86,merged87,merged88,merged89,merged90,merged91,merged92,merged93,merged94,merged95,merged96,merged97,merged98,merged99,merged100,merged101,merged102,merged103,merged104,merged105,merged106,merged107,merged108,merged109,merged110,merged111,merged112,merged113,merged114,merged115,merged116,merged117,merged118,merged119,merged120,merged121,merged122,merged123,merged124,merged125,merged126,merged127,merged128,merged129,merged130,merged131,merged132,merged133,merged134,merged135,merged136,merged137,merged138,merged139,merged140,merged141,merged142,merged143,merged144,merged145,merged146,merged147,merged148,merged149,merged150,merged151,merged152,merged153,merged154,merged155,merged156,merged157,merged158,merged159,merged160,merged161,merged162,merged163,merged164,merged165,merged166,merged167,merged168,merged169,merged170,merged171,merged172,merged173,merged174,merged175,merged176,merged177,merged178,merged179,merged180,merged181,merged182,merged183,merged184,merged185,merged186,merged187,merged188,merged189,merged190,merged191,merged192,merged193,merged194],axis="columns")
#single column name generator among n no of same column name
yabba.to_csv(r"D:\uvakai\Lakes verified\verification.csv")


# In[15]:


yabba2=pd.read_csv(r"D:\uvakai\Lakes verified\summaa.csv")
yabba3=pd.DataFrame(yabba2["aa"])
yabba3


# In[16]:


yabba4=yabba.drop("aa",axis="columns")
yabba4


# In[17]:


finalop=pd.concat([yabba3,yabba4],axis="columns")
finalop.to_csv(r"D:\uvakai\Lakes\full for verification.csv")
finalop


# In[19]:


ok1=finalop.drop("capacity",axis="columns")
ok1


# In[20]:


h1=[]
for x in range(1,195,1):
    a="wsa"
    b=str(x)
    c=a+b
    h1.append(c)
print(h1)


# In[21]:


ok2=ok1.drop("aa",axis="columns")
ok2.columns=h1
gg1=pd.concat([yabba3,ok2],axis="columns")
gg1


# In[22]:


ok3=finalop.drop("wsa",axis="columns")
ok3


# In[23]:


h2=[]
for x in range(1,195,1):
    a="capacity"
    b=str(x)
    c=a+b
    h2.append(c)
print(h2)


# In[24]:


ok4=ok3.drop("aa",axis="columns")
ok4


# In[25]:


ok4.columns=h2
ok4


# In[26]:


gg2=pd.concat([yabba3,ok4],axis="columns")
gg2.to_csv(r"D:\uvakai\Lakes\full capacity renamed.csv")


# In[27]:


gg2


# In[28]:


love1=[]
for x in gg2["capacity1"]:
    love1.append(x)
print(love1)
print()
print(max(love1))
print(type(love1[2]))


# In[29]:


love2=[]
for x in love1:
    aa=x/max(love1)
    bb=aa*100
    love2.append(bb)
print(love2)
max(love2)


# In[31]:


for x in range(1,195,1):
    globals()[f'oolove{x}']=[]
for x in range(1,195,1):
    globals()[f'pplove{x}']=[]
for x in range(1,195,1):
    globals()[f'tiger{x}']=[]


# In[32]:


for x in range(1,195,1):
    for y in gg2[h2[x-1]]:
        globals()[f'oolove{x}'].append(y)


# In[33]:


for x in range(1,195,1):
    for y in globals()[f'oolove{x}']:
        if y==y:
            globals()[f'tiger{x}'].append(y)


# In[34]:


for x in range(1,195,1):
    for y in globals()[f'oolove{x}']:
        qq=sum(globals()[f'tiger{x}'])
        if qq==0.0:
            globals()[f'pplove{x}'].append(y)
        else:
            aa=y/max(globals()[f'tiger{x}'])
            bb=aa*100
            if bb>=0 and bb<=20:
                globals()[f'pplove{x}'].append("0-20%")
            elif bb>20 and bb<=40:
                globals()[f'pplove{x}'].append("20-40%")
            elif bb>40 and bb<=60:
                globals()[f'pplove{x}'].append("40-60%")
            elif bb>60 and bb<=80:
                globals()[f'pplove{x}'].append("60-80%")
            elif bb>80 and bb<=100:
                globals()[f'pplove{x}'].append("80-100%")
            else:
                globals()[f'pplove{x}'].append(float('nan'))


# In[35]:


joshwin=[]
for x in range(1,195,1):
    a="lake"
    b=str(x)
    c=a+b
    joshwin.append(c)
print(joshwin)


# In[36]:


for x in range(1,195,1):
    globals()[f'dictt{x}']={joshwin[x-1]:globals()[f'pplove{x}']}


# In[37]:


for x in range(1,195,1):
    globals()[f'dataframebro{x}']=pd.DataFrame(globals()[f'dictt{x}'])


# In[38]:


siu=[]
for x in range(1,195,1):
    a="dataframebro"
    b=str(x)
    c=a+b
    siu.append(c)
tty=','.join(siu)
print(tty)


# In[39]:


vij=pd.concat([dataframebro1,dataframebro2,dataframebro3,dataframebro4,dataframebro5,dataframebro6,dataframebro7,dataframebro8,dataframebro9,dataframebro10,dataframebro11,dataframebro12,dataframebro13,dataframebro14,dataframebro15,dataframebro16,dataframebro17,dataframebro18,dataframebro19,dataframebro20,dataframebro21,dataframebro22,dataframebro23,dataframebro24,dataframebro25,dataframebro26,dataframebro27,dataframebro28,dataframebro29,dataframebro30,dataframebro31,dataframebro32,dataframebro33,dataframebro34,dataframebro35,dataframebro36,dataframebro37,dataframebro38,dataframebro39,dataframebro40,dataframebro41,dataframebro42,dataframebro43,dataframebro44,dataframebro45,dataframebro46,dataframebro47,dataframebro48,dataframebro49,dataframebro50,dataframebro51,dataframebro52,dataframebro53,dataframebro54,dataframebro55,dataframebro56,dataframebro57,dataframebro58,dataframebro59,dataframebro60,dataframebro61,dataframebro62,dataframebro63,dataframebro64,dataframebro65,dataframebro66,dataframebro67,dataframebro68,dataframebro69,dataframebro70,dataframebro71,dataframebro72,dataframebro73,dataframebro74,dataframebro75,dataframebro76,dataframebro77,dataframebro78,dataframebro79,dataframebro80,dataframebro81,dataframebro82,dataframebro83,dataframebro84,dataframebro85,dataframebro86,dataframebro87,dataframebro88,dataframebro89,dataframebro90,dataframebro91,dataframebro92,dataframebro93,dataframebro94,dataframebro95,dataframebro96,dataframebro97,dataframebro98,dataframebro99,dataframebro100,dataframebro101,dataframebro102,dataframebro103,dataframebro104,dataframebro105,dataframebro106,dataframebro107,dataframebro108,dataframebro109,dataframebro110,dataframebro111,dataframebro112,dataframebro113,dataframebro114,dataframebro115,dataframebro116,dataframebro117,dataframebro118,dataframebro119,dataframebro120,dataframebro121,dataframebro122,dataframebro123,dataframebro124,dataframebro125,dataframebro126,dataframebro127,dataframebro128,dataframebro129,dataframebro130,dataframebro131,dataframebro132,dataframebro133,dataframebro134,dataframebro135,dataframebro136,dataframebro137,dataframebro138,dataframebro139,dataframebro140,dataframebro141,dataframebro142,dataframebro143,dataframebro144,dataframebro145,dataframebro146,dataframebro147,dataframebro148,dataframebro149,dataframebro150,dataframebro151,dataframebro152,dataframebro153,dataframebro154,dataframebro155,dataframebro156,dataframebro157,dataframebro158,dataframebro159,dataframebro160,dataframebro161,dataframebro162,dataframebro163,dataframebro164,dataframebro165,dataframebro166,dataframebro167,dataframebro168,dataframebro169,dataframebro170,dataframebro171,dataframebro172,dataframebro173,dataframebro174,dataframebro175,dataframebro176,dataframebro177,dataframebro178,dataframebro179,dataframebro180,dataframebro181,dataframebro182,dataframebro183,dataframebro184,dataframebro185,dataframebro186,dataframebro187,dataframebro188,dataframebro189,dataframebro190,dataframebro191,dataframebro192,dataframebro193,dataframebro194],axis="columns")
vij


# In[40]:


wsafinal=pd.concat([yabba3,vij],axis="columns")
wsafinal.to_csv(r"D:\uvakai\Lakes verified\dg.csv")


# In[111]:


duplicateremoved5


# In[112]:


for i in range(1,195,1):
    globals()[f'grace{i}'] =[]


# In[113]:


mathi=[]
for x in yabba3["aa"]:
    mathi.append(x)
print(len(mathi))


# In[114]:


jobi1=pd.concat([duplicateremoved1,duplicateremoved2,duplicateremoved3,duplicateremoved4,duplicateremoved5,duplicateremoved6,duplicateremoved7,duplicateremoved8,duplicateremoved9,duplicateremoved10,duplicateremoved11,duplicateremoved12,duplicateremoved13,duplicateremoved14,duplicateremoved15,duplicateremoved16,duplicateremoved17,duplicateremoved18,duplicateremoved19,duplicateremoved20,duplicateremoved21,duplicateremoved22,duplicateremoved23,duplicateremoved24,duplicateremoved25,duplicateremoved26,duplicateremoved27,duplicateremoved28,duplicateremoved29,duplicateremoved30,duplicateremoved31,duplicateremoved32,duplicateremoved33,duplicateremoved34,duplicateremoved35,duplicateremoved36,duplicateremoved37,duplicateremoved38,duplicateremoved39,duplicateremoved40,duplicateremoved41,duplicateremoved42,duplicateremoved43,duplicateremoved44,duplicateremoved45,duplicateremoved46,duplicateremoved47,duplicateremoved48,duplicateremoved49,duplicateremoved50,duplicateremoved51,duplicateremoved52,duplicateremoved53,duplicateremoved54,duplicateremoved55,duplicateremoved56,duplicateremoved57,duplicateremoved58,duplicateremoved59,duplicateremoved60,duplicateremoved61,duplicateremoved62,duplicateremoved63,duplicateremoved64,duplicateremoved65,duplicateremoved66,duplicateremoved67,duplicateremoved68,duplicateremoved69,duplicateremoved70,duplicateremoved71,duplicateremoved72,duplicateremoved73,duplicateremoved74,duplicateremoved75,duplicateremoved76,duplicateremoved77,duplicateremoved78,duplicateremoved79,duplicateremoved80,duplicateremoved81,duplicateremoved82,duplicateremoved83,duplicateremoved84,duplicateremoved85,duplicateremoved86,duplicateremoved87,duplicateremoved88,duplicateremoved89,duplicateremoved90,duplicateremoved91,duplicateremoved92,duplicateremoved93,duplicateremoved94,duplicateremoved95,duplicateremoved96,duplicateremoved97,duplicateremoved98,duplicateremoved99,duplicateremoved100,duplicateremoved101,duplicateremoved102,duplicateremoved103,duplicateremoved104,duplicateremoved105,duplicateremoved106,duplicateremoved107,duplicateremoved108,duplicateremoved109,duplicateremoved110,duplicateremoved111,duplicateremoved112,duplicateremoved113,duplicateremoved114,duplicateremoved115,duplicateremoved116,duplicateremoved117,duplicateremoved118,duplicateremoved119,duplicateremoved120,duplicateremoved121,duplicateremoved122,duplicateremoved123,duplicateremoved124,duplicateremoved125,duplicateremoved126,duplicateremoved127,duplicateremoved128,duplicateremoved129,duplicateremoved130,duplicateremoved131,duplicateremoved132,duplicateremoved133,duplicateremoved134,duplicateremoved135,duplicateremoved136,duplicateremoved137,duplicateremoved138,duplicateremoved139,duplicateremoved140,duplicateremoved141,duplicateremoved142,duplicateremoved143,duplicateremoved144,duplicateremoved145,duplicateremoved146,duplicateremoved147,duplicateremoved148,duplicateremoved149,duplicateremoved150,duplicateremoved151,duplicateremoved152,duplicateremoved153,duplicateremoved154,duplicateremoved155,duplicateremoved156,duplicateremoved157,duplicateremoved158,duplicateremoved159,duplicateremoved160,duplicateremoved161,duplicateremoved162,duplicateremoved163,duplicateremoved164,duplicateremoved165,duplicateremoved166,duplicateremoved167,duplicateremoved168,duplicateremoved169,duplicateremoved170,duplicateremoved171,duplicateremoved172,duplicateremoved173,duplicateremoved174,duplicateremoved175,duplicateremoved176,duplicateremoved177,duplicateremoved178,duplicateremoved179,duplicateremoved180,duplicateremoved181,duplicateremoved182,duplicateremoved183,duplicateremoved184,duplicateremoved185,duplicateremoved186,duplicateremoved187,duplicateremoved188,duplicateremoved189,duplicateremoved190,duplicateremoved191,duplicateremoved192,duplicateremoved193,duplicateremoved194],axis="columns")
jobi1


# In[115]:


jobi2=jobi1["aa"]
jobi2


# In[116]:


jobi2.columns=joshwin
jobi2


# In[117]:


for x in range(1,195,1):
    globals()[f'pepsilist{x}']=[]


# In[118]:


for x in range(1,195,1):
    for y in jobi2[joshwin[x-1]]:
        globals()[f'pepsilist{x}'].append(y)


# In[119]:


pq=[]
for x in yabba3["aa"]:
    pq.append(x)
print(pq)


# In[120]:


for x in range(1,195,1):
    globals()[f'grass{x}']=[]


# In[127]:


for x in range(1,195,1):
    for y in pq:
        if y not in globals()[f'pepsilist{x}']:
            globals()[f'grass{x}'].append(y)
        else:
            continue


# In[134]:


len(grass67)


# In[140]:


for x in range(1,195,1):
    globals()[f'dictt{x}']={joshwin[x-1]:globals()[f'grass{x}']}


# In[141]:


for x in range(1,195,1):
    globals()[f'dataframegirl{x}']=pd.DataFrame(globals()[f'dictt{x}'])


# In[144]:


ppp=pd.concat([dataframegirl1,dataframegirl2,dataframegirl3,dataframegirl4,dataframegirl5,dataframegirl6,dataframegirl7,dataframegirl8,dataframegirl9,dataframegirl10,dataframegirl11,dataframegirl12,dataframegirl13,dataframegirl14,dataframegirl15,dataframegirl16,dataframegirl17,dataframegirl18,dataframegirl19,dataframegirl20,dataframegirl21,dataframegirl22,dataframegirl23,dataframegirl24,dataframegirl25,dataframegirl26,dataframegirl27,dataframegirl28,dataframegirl29,dataframegirl30,dataframegirl31,dataframegirl32,dataframegirl33,dataframegirl34,dataframegirl35,dataframegirl36,dataframegirl37,dataframegirl38,dataframegirl39,dataframegirl40,dataframegirl41,dataframegirl42,dataframegirl43,dataframegirl44,dataframegirl45,dataframegirl46,dataframegirl47,dataframegirl48,dataframegirl49,dataframegirl50,dataframegirl51,dataframegirl52,dataframegirl53,dataframegirl54,dataframegirl55,dataframegirl56,dataframegirl57,dataframegirl58,dataframegirl59,dataframegirl60,dataframegirl61,dataframegirl62,dataframegirl63,dataframegirl64,dataframegirl65,dataframegirl66,dataframegirl67,dataframegirl68,dataframegirl69,dataframegirl70,dataframegirl71,dataframegirl72,dataframegirl73,dataframegirl74,dataframegirl75,dataframegirl76,dataframegirl77,dataframegirl78,dataframegirl79,dataframegirl80,dataframegirl81,dataframegirl82,dataframegirl83,dataframegirl84,dataframegirl85,dataframegirl86,dataframegirl87,dataframegirl88,dataframegirl89,dataframegirl90,dataframegirl91,dataframegirl92,dataframegirl93,dataframegirl94,dataframegirl95,dataframegirl96,dataframegirl97,dataframegirl98,dataframegirl99,dataframegirl100,dataframegirl101,dataframegirl102,dataframegirl103,dataframegirl104,dataframegirl105,dataframegirl106,dataframegirl107,dataframegirl108,dataframegirl109,dataframegirl110,dataframegirl111,dataframegirl112,dataframegirl113,dataframegirl114,dataframegirl115,dataframegirl116,dataframegirl117,dataframegirl118,dataframegirl119,dataframegirl120,dataframegirl121,dataframegirl122,dataframegirl123,dataframegirl124,dataframegirl125,dataframegirl126,dataframegirl127,dataframegirl128,dataframegirl129,dataframegirl130,dataframegirl131,dataframegirl132,dataframegirl133,dataframegirl134,dataframegirl135,dataframegirl136,dataframegirl137,dataframegirl138,dataframegirl139,dataframegirl140,dataframegirl141,dataframegirl142,dataframegirl143,dataframegirl144,dataframegirl145,dataframegirl146,dataframegirl147,dataframegirl148,dataframegirl149,dataframegirl150,dataframegirl151,dataframegirl152,dataframegirl153,dataframegirl154,dataframegirl155,dataframegirl156,dataframegirl157,dataframegirl158,dataframegirl159,dataframegirl160,dataframegirl161,dataframegirl162,dataframegirl163,dataframegirl164,dataframegirl165,dataframegirl166,dataframegirl167,dataframegirl168,dataframegirl169,dataframegirl170,dataframegirl171,dataframegirl172,dataframegirl173,dataframegirl174,dataframegirl175,dataframegirl176,dataframegirl177,dataframegirl178,dataframegirl179,dataframegirl180,dataframegirl181,dataframegirl182,dataframegirl183,dataframegirl184,dataframegirl185,dataframegirl186,dataframegirl187,dataframegirl188,dataframegirl189,dataframegirl190,dataframegirl191,dataframegirl192,dataframegirl193,dataframegirl194],axis="columns")


# In[146]:


ppp.to_csv(r"D:\uvakai\Lakes verified\vannamathi.csv")

