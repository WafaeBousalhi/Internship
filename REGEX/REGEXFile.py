#!/usr/bin/env python
# coding: utf-8
Question 1
# In[279]:


import regex as re
string1 = "Python Exercises, PHP exercises."
pattern1 = r'[,\.\s]'
answer1 = re.sub(pattern,':',string)
print(answer1)

Question 2
# In[328]:


import pandas as pd
dict1 = {'Summary':['hello, world!', 'XXXXX test', '123four, five:; six...']}
df2 = pd.DataFrame(dict1)
pattern2 = r'[^a-z\s]+'

answer2 = df2['Summary'].str.replace(pattern2 , lambda m : '', regex = True )
print(answer2)

Question 3
# In[532]:


answer3 = re.compile(r'\b\w{4,}\b')
string3 =  'I am someone that eats halo'
print(answer3.findall(string3))

Question4
# In[536]:


answer4 = re.compile(r'\b\w{4,5}\b')
string4 =  'I am someone that eats haloe'
print(answer4.findall(string4))

Question 5
# In[531]:


pattern5 = re.compile(r'[^\s()]+')
string5 = ["example (.com)", "hr@fliprobo (.com)", "github (.com)", "Hello (Data Science World)", "Data (Scientist)"]

for s5 in string5:
    answer5 = pattern5.findall(s5)
    print(''.join(answer5))

Question 6
# In[254]:


pattern4 = re.compile(r'^[^()]+')
string4 = ["example (.com)", "hr@fliprobo (.com)", "github (.com)", "Hello (Data Science World)", "Data (Scientist)"]

for s in string4:
    answer4 = pattern4.findall(s)
    print(''.join(answer4))

Question 7
# In[289]:


string7 =  'ImportanceOfRegularExpressionsInPython'
answer7 = re.split(r'(?=[A-Z])',string7)
print(answer7)

Question 8
# In[294]:


string8 =  'RegularExpression1IsAn2ImportantTopic3InPython'
answer8 = re.sub(r'(?=\d+)'," ",string8)
print(answer8)


Question 9: 
There are two answers for question 9.

The first answer follows the instructions defined in the question, by inserting a space between words that start with a number or a capital letter (answer 9a)

The second answer gives the same output as the expected output by inserting a space before and after any number present in the string (answer9b)
# In[327]:


string9a =  'RegularExpression1IsAn2ImportantTopic3InPython'
answer9a = re.sub(r'(?=[A-Z]|[\d])'," ",string9a)
print(answer9a)

string9b =  'RegularExpression1IsAn2ImportantTopic3InPython'
answer9b = re.sub(r'(?=[\d])|(?<=[\d])'," ",string9b)
print(answer9b)

Question 10
# In[340]:


df10 = pd.read_csv("https://raw.githubusercontent.com/dsrscientist/DSData/master/happiness_score_dataset.csv")
pattern10 = r'^([a-zA-Z]{6})'
df10['first_five_letters'] = df10['Country'].str.extract(pattern10)

print(df10['first_five_letters'])

Question 11
# In[343]:


answer11 = re.compile(r'\w+')
string11 =  ['I love','2c5', 'that there are','_ a fe','$% thi*(op)']

for s in string11:
    print(re.match(answer11,s))


# In[ ]:


Question 12
The specific number chosen for this question


# In[346]:


answer12 = re.compile(r'2')
string12 =  ['I love','2c5', 'that there are','_ a fe','$% thi*(op)']

for s12 in string12:
    print(re.match(answer12,s12))


# In[ ]:


Question 13

Two ways to remove zeroes from IP address


# In[362]:


answer13 = r'0'
string13 = '061.035.025.142'

print(string13.replace(answer13,""))
      
answer13 = r'0'
string13 = '061.035.025.142'

print(re.sub(answer13,"",string13))


# In[ ]:


Question 14


# In[375]:


answer14 = r'\w+\s\d{1,2}[a-z]{2}\s\d{4}'
string14 = 'On August 15th 1947 that India was declared independent from British colonialism, and the reins of control were handed over to the leaders of the Country'


print(re.search(answer14,string14))


# In[ ]:


Question 15

What I understood from the question is to search for some literal strings with a criteria 
defined by myself (from 3 to 4 characters) in a string 


# In[382]:


pattern15 = r'(\b[a-zA-Z]{3,4}\b)'
string15 = 'The quick brown fox jumps over the lazy dog.'
answer15 = re.finditer(pattern15,string15)

for s15 in answer15:
    print(s15.group(1))


# In[ ]:


Question 16


# In[383]:


pattern16 = r'fox'
string16 = 'The quick brown fox jumps over the lazy dog.'
answer16 = re.search(pattern16,string16)

print('The match is:', answer16.group())
print('The start location:', answer16.start())
print('The end location:', answer16.end())


# In[ ]:


Question 17


# In[386]:


pattern17 = r'exercises'
string17 = 'Python exercises, PHP exercises, C# exercises'
answer17 = re.search(pattern17,string17)
answer17


# In[ ]:


Question 18


# In[390]:


pattern18 = r'exercises'
string18 = 'Python exercises, PHP exercises, C# exercises'
answer18 = re.finditer(pattern18,string18)

for match18 in answer18:
    print('The match is:', match18.group())
    print('The start location:', match18.start())
    print('The end location:', match18.end())


# In[ ]:


Question 19


# In[391]:


answer13 = r'(\d{4})-(\d{2})-(\d{2})'
string13 = 'I was born in 1998-12-28 in a city in Norther Scotland'

print(re.sub(answer13,r'\3-\2-\1',string13))


# In[ ]:


Question 20


# In[530]:


answer20 = re.compile(r'\b\d+\.\d{1,2}\b') 

string20 =  '01.12 0132.123 2.31875 145.8 3.01 27.25 0.25'
print(answer20.findall(string20))


# In[ ]:


Question 21


# In[398]:


string21 =  'RegularExpression1IsAn2ImportantTopic3InPython'
pattern21 = r'\d+'
answer21 = re.finditer(pattern21,string21)

for match21 in answer21:
    print('The match is:', match21.group())
    print('The start location:', match21.start())
    print('The end location:', match21.end())


# In[ ]:


Question 22


# In[425]:


string22 = 'My marks in each semester are: 947, 896, 926, 524, 734, 950, 642'
pattern22 = r'\d+'
regex22 = re.finditer(pattern22,string22)

list22 = []

for match22 in regex22:
    list22.append(int(match22.group()))

if list22:
    answer22 = max(list22)
    print(answer22)


# In[ ]:


Question 23


# In[426]:


string23 =  'RegularExpressionIsAnImportantTopicInPython'
answer23 = re.sub(r'(?=[A-Z])', ' ', string23)
print(answer23)


# In[ ]:


Question 24


# In[504]:


string24 = 'Regular Expression Is AnImportantTopicInPython'
pattern24 = r'[A-Z][a-z]+'
answer24 = re.findall(pattern24, string24)


for match24 in answer24:
    print(match24)


# In[ ]:


Question 25


# In[505]:


pattern25 = r'\b(\w+)(\s\1\b)'
string25 = "Hello hello world world"

answer25 = re.sub(pattern25, r'\1', string25)

print(answer25)


# In[ ]:


Question 26


# In[511]:


pattern26 = r'[a-zA-Z0-9]$'
string26a = "Hello hello world world0"
string26b = "Hello hello world world*"

answer26a = re.findall(pattern26, string26a)
answer26b = re.findall(pattern26, string26b)

if answer26a:
    print('Accept the string')
else:
    print('Do not accept the string')

if answer26b:
    print('Accept the string')
else:
    print('Do not accept the string')


# In[ ]:


Question 27


# In[513]:


string27 = """RT @kapil_kausik: #Doltiwal I mean #xyzabc is "hurt" by #Demonetization as the same has rendered USELESS <ed><U+00A0><U+00BD><ed><U+00B1><U+0089> "acquired funds" No wo"""
pattern27 = r'#\w+'

answer27 = re.findall(pattern27,string27)
print(answer27)


# In[ ]:


Question 28


# In[526]:


string28 = "@Jags123456 Bharat band on 28??<ed><U+00A0><U+00BD><ed><U+00B8><U+0082>Those who  are protesting #demonetization  are all different party leaders"
pattern28 = r'<U\+\w+>'

answer28 = re.sub(pattern28, '', string28)
print(answer28)


# In[ ]:


Question 29


# In[521]:


string29 = 'Ron was born on 12-09-1992 and he was admitted to school 15-12-1999.'
pattern29 = '\d{1,2}-\d{1,2}-\d{4}'

answer29 = re.findall(pattern29, string29)
print(answer29)


# In[ ]:


Question 30


# In[528]:


string30 = "The following example creates an ArrayList with a capacity of 50 elements. 4 elements are then added to the ArrayList and the ArrayList is trimmed accordingly."
pattern30 = re.compile(r'\b\w{2,4}\b')

answer30 = pattern30.sub('', string30)
print(answer30)

