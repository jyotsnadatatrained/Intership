#!/usr/bin/env python
# coding: utf-8

# In[39]:


#Question 1- Write a Python program to replace all occurrences of a space, comma, or dot with a colon.
#Sample Text- 'Python Exercises, PHP exercises.'
#Expected Output: Python:Exercises::PHP:exercises:

#solution

import re

string = 'Hi there, my name is Jyotsna.'
pattern = r'[\s.,]'

replace = ':'
result = re.sub(pattern,replace,string)
print(result)


# In[24]:


#Question 2- Write a Python program to find all words starting with 'a' or 'e' in a given string.

import re

string = 'An elephant is eating an apple'
pattern = r'\b[AaEe]\w+\b'
result = re.findall(pattern,string)
print('\n Words starting with a or e \n','-'*50)
print(result)


# In[28]:


#Question 3- Create a function in python to find all words that are at least 4 characters long in a string.
#The use of the re.compile() method is mandatory.

string = 'Happy weds dogs and cat'
pattern = re.compile(r'\b\w{4,}\b')
result = pattern.findall(string)
print(result)


# In[33]:


#Question 4- Create a function in python to find all three, four, and five character words in a string.
#The use of the re.compile() method is mandatory.

string = 'This is the best time of my life so cheers and be grateful'
pattern = re.compile(r'\b\w{3,6}\b')
result = pattern.findall(string)
print(result)


# In[131]:


#question 5 Create a function in Python to remove the parenthesis in a list of strings. 
#The use of the re.compile() method is mandatory.




# In[12]:


#Question 6- Write a python program to remove the parenthesis area from the text stored 
#in the text file using Regular Expression.

import re
pattern = r' ?\([^)]+\)'
strings = ["google (.com)", "float (.com)", " (.com)"]
for string in strings:
    print(re.sub(r' \([^)]+\)', '',string))


# In[44]:


#Question 7- Write a regular expression in Python to split a string into uppercase letters.

import re

string = "HiMyNameIsNidhi"
result = re.split(r"(?=[A-Z])", string)
print(result)


# In[49]:


#Question 8- Create a function in python to insert spaces between words starting with numbers.

string = 'There are 2books and 4apples on the table'
pattern = r'(\b\d+)(\w+)'
replace = r'\1 \2 '
result = re.sub(pattern, replace, string)
print(result)


# In[8]:


#Question 9- Create a function in python to insert spaces between words starting with capital letters or with numbers.

#google

import re

def insert_spaces(text):
    # Use regex to find words starting with capital letters or numbers
    pattern = r'([A-Z][a-z0-9]+|[0-9]+)'
    matches = re.findall(pattern, text)
    
    # Insert spaces before the matched words
    for match in matches:
        text = re.sub(match, ' ' + match, text)
    
    return text
text = "ThisIsAnExample123"
formatted_text = insert_spaces(text)
print(formatted_text)


# In[11]:


#ques10



# In[4]:


#Question 11- Write a Python program to match a string that contains only upper and lowercase letters, 
#numbers, and underscores.

string = "Jyotsna_jha123"
pattern = '^[A-Za-z0-9_]*$'
result = re.search(pattern, string)
print(result)



# In[6]:


#Question 12- Write a Python program where a string will start with a specific number. doubt

string = '2djbjcdnknck'
pattern = r'^2'
result = re.match(pattern,string)
print(result)


# In[24]:


#Question 13- Write a Python program to remove leading zeros from an IP address

import re
string = '234.001.023.145.546'
pattern = r'\b0+(\d)'
replace = r'\1'
result = re.sub(pattern,replace,string)
print(result)


# In[ ]:


#Question 14- Write a regular expression in python to match a date string in the form of 
#Month name followed by day number and year stored in a text file.




# In[67]:


#Question 15- Write a Python program to search some literals strings in a string. 

import re
literals = ['mat','cat','rat','door']
string = 'The cat and rat are on the mat and the car is parked outside.'
for literal in literals:
    print(literal,string)
    if re.search(literal, string):
        print('Matched')
    else:
        print('Not Matched')


# In[27]:


#Question 16- Write a Python program to search a literals string in a string and 
#also find the location within the original string where the pattern occurs
string = 'The cat sat on a mat'
pattern = 'sat'
result = re.search(pattern, string)
a = result.start()
b = result.end()
print('Searched for "%s" in "%s" from %d to %d ' % \
     (pattern, string, a, b))


# In[46]:


#Question 17- Write a Python program to find the substrings within a string.


string = 'This is good, Life is good, Tea is perfect'
pattern = 'good'
result = re.findall(pattern,string)
print(result)


# In[30]:


#Question 18- Write a Python program to find the occurrence and position of the substrings within a string.
import re

string = 'This is good, Life is good, Tea is perfect'
pattern = 'good'
for search in re.finditer(pattern, string):
    a = search.start()
    b = search.end()
    print('Match "%s" at %d:%d' % (string[a:b], a, b))


# In[38]:


#Question 19- Write a Python program to convert a date of yyyy-mm-dd format to dd-mm-yyyy format.

string_date = '2023-11-21'
pattern = r'(\d{4})-(\d{2})-(\d{2})'
replace = r'\3-\2-\1'
result = re.sub(pattern, replace, string_date)
print(result)


# In[12]:


#Question 20- Create a function in python to find all decimal numbers with a precision of 1 or 2 in a string. 
#The use of the re.compile() method is mandatory
string = 'The prices are $10.5, $20.75, and $30.8.'
pattern = re.compile('\d+\.\d{1,2}')
result = re.findall(pattern, string)
print(result)


# In[50]:


#Question 21- Write a Python program to separate and print the numbers and their position of a given string.

string = 'He has 4 apples and 3 bananas'
pattern = '\d+'
for search in re.finditer(pattern, string):
    print(search.group(0))
    print(" Index position of the given number:", search.start())



# In[70]:


#Question 22- Write a regular expression in python program to extract maximum/largest numeric value from a string.

def max_numeric(string):
    string = 'He has 4 apples and 2 bananas'
    pattern = r'\d+'
    results = re.findall(pattern, string)
    numbers = [int(result) for result in results]
    max_number =  max(numbers)
    return max_number
max_value = max_numeric(string) 
print('Max value is:', max_value)


# In[9]:


#Question 23- Create a function in python to insert spaces between words starting with capital letters.

string = 'HappyUsIsTheRealUs'
pattern = r'(\w)([A-Z])'
replace = r'\1 \2'
result = re.sub(pattern, replace, string)
print(result)


# In[32]:


#Question 24- Python regex to find sequences of one upper case letter followed by lower case letters

string = 'Time will Heal everything'
pattern = r'[A-Z][a-z]+'
result = re.findall(pattern,string)
print(result)


# In[78]:


#Question 25- Write a Python program to remove continuous duplicate words from Sentence using Regular Expression.

string = 'This is hello hello set set.'
pattern = r'\b(\w+)\s\1\b'
result = re.sub(pattern, r'\1', string)
print(result)


# In[85]:


#Question 26-  Write a python program using RegEx to accept string ending with alphanumeric character.

def end_with_alphanumeric(string):
    pattern = r'[a-zA-Z0-9]$'
    result = re.search(pattern, string)
    if result:
        return True
    else:
        return False
string1 = 'Jyotsna123'
string2 = 'ghsdh$'
string3 = '12344'
string4 = 'happy12'
    
print(end_with_alphanumeric(string1))
print(end_with_alphanumeric(string2))
print(end_with_alphanumeric(string3))
print(end_with_alphanumeric(string4))


# In[63]:


#Question 27-Write a python program using RegEx to extract the hashtags.

string = 'He hates #gaming and loves #swimmming as #hobbies' 
pattern = r'\#\w+'
result = re.findall(pattern, string)
print(result)


# In[107]:


#Question 28- Write a python program using RegEx to remove <U+..> like symbols


string= 'Hey <U+adg123> there <U+dg65> !'
pattern = r'<U\+[a-g0-9]+>'
replace = ''
result = re.sub(pattern, replace, string)
print(result)
    


# In[128]:


#Question 29- Write a python program to extract dates from the text stored in the text file.

import pandas as pd
text = pd.read_csv(r'https://raw.githubusercontent.com/jyotsnadatatrained/MY-REPO/main/Book1.csv')
text


# In[66]:


#Question 30- Create a function in python to remove all words from a string of length between 2 and 4.

string = 'Hi my name is Nidhi and i am a great personality'
pattern = r'\b\w{2,4}\b'
result = re.sub(pattern,'',string)
print(result)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




