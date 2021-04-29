#!/usr/bin/env python
# coding: utf-8

# In[1]:


# This is a simple program that counts
# Total Words in a file, 
# Number of upper case word in the file
# and unique word in the file

## Author Abdul Basit
## github.com/elbasit
## elbasit23@gmail.com

file = open("Lorem_ipsum.txt", "rt")
data = file.read()
this = data.split()

print('Number of words in text file :', len(this))

capital = 0
count = {}
string = []

# Coverting the list into string list
for word in this:
    string.append(str(word))

for word in string:
    
    if word in count:       
       count[word] += 1

    else:
      count[word] = 1

# Counting the Capital Words
res = [word for word in string if word.isupper()]

print('Total count of every word in the text is :\n',count)
print('Number of unique words in the text are : \n',len(count))

print("The uppercase characters in string are : \n" , str(res))
print("The number of uppercase words in string are :\n " , len((res)))


# In[ ]:




