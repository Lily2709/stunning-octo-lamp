#!/usr/bin/env python
# coding: utf-8

# In[1]:


print("Hello World")


# In[1]:


public class Main {
  public static void main(String[] args) {
    System.out.println("Hello, World!");
  }
}


# In[7]:


பதிப்பி "உலகே வணக்கம்"
பதிப்பி "Hello, World!"
exit()


# In[6]:


#include <iostream>

int main()
{
  std::cout << "Hello, World!\n";
  return 0;
}


# In[8]:


#the scripts report a syntax error because I am using a python environment, therefore other languages cannot run


# In[1]:


print("Lily Plotkin")


# In[2]:


print(" ")


# In[3]:


print(len("Python"))


# In[5]:


a = "My favorite number is nine."
print(len(a))


# In[6]:


b = "In 2022, Python 3.10.4 and 3.9.12 were expedited and so were older releases including 3.8.13, and 3.7.13 becuase of many security issues in 2022. Python 3.9.13 is the latest 3.9 version, and from now on 3.9 (and older; 3.8 and 3.7) will only get security updates."
print(len(b))


# In[22]:


print(9988870*303)


# In[23]:


print(34199820/2121.4)


# In[24]:


print(9988870+34199820+2121.4)


# In[33]:


#I interpreted the "divided by 2" to mean the whole thing divided by 2, I'm not sure if this is what you were looking for
print((9988870+34199820+2121.4)/2)


# In[32]:


print((130+45-12)/(98*2))


# In[31]:


print(332403650-332524270)


# In[30]:


#output is the number of teams
print(325/6)


# In[29]:


#output is how many participants will work in a team with fewer participants
print(325%6)


# In[18]:


import math


# In[28]:


print(math.log(10))


# In[26]:


print(math.sqrt(255))


# In[25]:


print(math.gcd(200, 25))


# In[68]:


#output is number of complete teams for hackathon
print(325//6)


# In[37]:


#output is number of ppts with fewer in a group
print(math.remainder(325, 6))


# In[40]:


89==87


# In[41]:


a = 332433240365003633240365050
a != a


# In[43]:


a == a


# In[45]:


89>89


# In[46]:


89==89


# In[47]:


89>= 89


# In[48]:


89<=89


# In[49]:


89=='89'


# In[50]:


89!='89'


# In[51]:


True == True


# In[52]:


True == "True"


# In[54]:


'Hello World!' == 'Hello World!'


# In[58]:


a = "In 2022, Python 3.10.4 and 3.9.12 were expedited and so were older releases including 3.8.13, and 3.7.13 because of many security issues in 2022. Python 3.9.13 is the latest 3.9 version, and from now on 3.9 (and older; 3.8 and 3.7) will only get security updates."
b = "In 2021, Python 3.10.4 and 3.9.12 were expedited and so were older releases including 3.8.13, and 3.7.13 because of many security issues in 2022. Python 3.9.13 is the latest 3.9 version, and from now on 3.9 (and older; 3.8 and 3.7) will only get security updates."
a == a


# In[59]:


a == b


# In[63]:


print("I am turning "+str(19)+" on September "+str(27)+"th, "+str(2022)+".")


# In[67]:


print("I am turning '+"19"+"on September str(27)th"+ 2022.)
#1. need to close parenthesis with consistent type. I did "' when it should either be "" or ''
#2. I put 19 in quotes without properly converting the number to a string with the str() function
#3. I did str(27) but inside the existing string but you can't do this becuase it will print it as str(27) in the final output instead of just the number
#4. The "th" after str(27) should not be there, str() function and strings/words should be separated 
#5. 2022 is not in any string form or even in quotes, needs to be converted to a string before being able to be added to the sentence string







