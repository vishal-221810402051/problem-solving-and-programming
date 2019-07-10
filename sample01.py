#!/usr/bin/env python
# coding: utf-8

# In[1]:


print("hello gitam")


# In[ ]:





# In[2]:


print("hello gitam")
print("hyderabad")


# In[8]:


print("hello gitam"," ||| " ,end = " ")
print("hyderabad" , end=" ||| ")
print("python programming")      


# In[9]:


n1 = 100
a = b = c = 20
a1,b1,c1 = 111, 222, 333
print(n1)
print(a,b,c)
print(a1,b1,c1)


# In[10]:


a = 100;
s1 = "python"
s2 = 'p'
f1 = 10.2
print(a,s1,s2,f1)
print(type(a),type(s1),type(s2),type(f1))


# # Reading a value--Input Function
# ## . input("Message")--string

# In[13]:


#want a number as a input
n1 = int(input("enter a number"))
print(n1,type(n1))


# ## operators
# #### . operator is used to find some operations
# ### arthematic operations

# 
# ### +
# ### -
# ### *
# ### /
# ### % 
# ### //
# ### **

# In[14]:


n1 = 1234
print(n1+10)
print(n1-10)
print(n1*10)
print(n1/10)
print(n1%10)
print(n1//10)
print(n1**10)


# # Precedence of arth operations
# ### . parenthisis
# ### . Power
# ### .  muliplication 
# ### . addition
# ## left to right

# In[15]:


x = 1 + 2 ** 3 / 4 + 5
print(x)


# In[16]:


x = 1 + 2 ** 3 / 4 * 5
print(x)


# # Control flow statements
# ### .contidional statements
# ### .looping statements
# 
# ## .if-else statements
#  **syntax**
#  - ***if Boolean_condition:***
#  - **Statements**
#  - ***else:***
#  - **statements**
#  

# In[1]:


n = int(input("enter the value"))
if n%2==0:
    print("entered is even")
else:
    print ("odd")


# In[2]:


n= int(input("enter a number"))
if n%3==0 and n%5==0:
    print ("multiple of 3 and 5")
else:
    print ("no")


# In[3]:


#test the given number is positive ,negative,zero
n = int(input("enter the value"))
if n==0:
    print("zero")
if n<0:
    print("negative")
else :
    print("positive")


# In[1]:


#check weather the year is leap year or not
year = int(input("enter any year"))
if year%4==0:
    print("year is leap year")
else:
    print("not a leap year")
    


# In[3]:


n1= int(input("enter a number"))
n2= int(input("enter a number"))
n3= int(input("enter a number"))
if n1>n2 and n1<n3:
    print ("n1 is greater" +n1)
if n2>n1 and n2<n3:
    print ("n2 is greater" +n2)
else :
    print ("n3 is greater" +n3)


# In[5]:


#natural numbers
n=int(input("enter a number"))
i=1
while i<=n:
    print(i)
    i=i+1


# In[7]:


n= int(input("enter the number"))
i=1
sum =0
while i<=n:
    if i%2==0:
    sum = sum + i
i=i+1
print(sum)


# In[ ]:


def addEvenDigits(n):
    sum=0
    while n!=0
    r=n%


# In[13]:


def printLarge(n):
    large=0
    while n !=0:
        r =n%10
        if large <r:
            large =r
        n=n //10
    return large
 printLarge(19528)


# In[17]:


def reverseNumber(n):
    rev=0
    while n!=0:
        r =n%10
        rev=rev*10+r
        n=n//10
    return
reverseNumber(123)


# In[18]:


def isPalindrome(n):
    rev=0
    buffer=n
    while n!=0:
        r =n%10
        rev=rev*10+r
        n=n//10
    if buffer ==rev:
        return("yes")
    else:
        return("no")
reverseNumber(123)


# In[ ]:


def printSeries(l1,l1)
 for x in range (l1,ub=1)


# In[4]:


#find the factor of the given number
#12 -->1 2 3 4 6 12
 def factorList(n):
        for i in range (1,n+1):
            if n%i==0:
                print(i,end=" ")
        return
    factorList(12)


# In[8]:


# given number is prime or not
def isPrime(n):
    flag=True
    for i in range (2,n//2+1):
        if n%i==0:
            flag=False
            return flag
    return flag
isPrime(11)
    


# In[12]:


# function to find prime numbers from 1 to 10
def primeCount(n):
    cnt =0
    for a in range (2,n+1):
        k=0
        for i in range (2,a//2+1):
            if a%i==0:
                k=k+1
        if (k<=0):
            cnt=cnt+1
    return cnt
primeCount(10)


# In[ ]:


def factorial(n):
    fact = 1
    for i in range(2,n+1):
        fact*=i
        return fact
    def digitalFactSum(n):
        sum=0
        buffer = n
        while 


# #  Programming in python

# In[22]:


st = 'python'
print(st[0])
print(st[1])
print(st[3])
print(st[len(st)-1])
print(st[-1])
print(st[0:3])
print(st[-3:])


# In[23]:


#function to print upper case characters
#Example python -- P T
#ASCII:-
#A - Z : 65 - 90
#a - z : 97 - 122
#0 - 9 : 48 - 57
#space : 32
def printUpper(n):
    for i in range(lan(x)):
        if ord(x[i])""


# In[ ]:


x ="python"
print (str[-2::-2])


# In[26]:


x=10
s=str(x)
type(s)


# In[27]:


start = 11
end = 20
for x in range(start,end+1):
    if x+8 == end+1:
        print("python")
        break
    else:
        print("100")


# # day objective
# ### Python data structures
# #### Lists
# ### .Dictionries
# ### .Basic programs on data structures
# ### .ADVANCED problem Sets
# ### .Contact Applications (Dictionary Objectives)
# 
# # Data Structures
# ### .To store search and sort data
# 
# 
# # Python Data Structures
# ## list
# 
# ### .it's one of the common data structures supported by python ,the list items are seperated by comma and operator and enclosed in square brackets
# 
# ### .Example
# #### .list 1=[1,6,2,18,4]
# #### .list 2=["Gitam",10,12,15,"hyderabad"]

# In[4]:


lst =[1,8,16,9,2]
print(lst) #Access the entire list
print(lst[0]) #access the first list
print(lst[1]) #access the second list
print(lst[-1])#access the last list
print(lst[-2])
print(lst[1:])
print(lst[0:3])


# In[5]:


#Update the list values using index
li = ["Gitam","python",1989,2002]
print(li)
li[2] = 2019
print (li)


# In[6]:


# Delete the specific item in the list
print (li)
del li[2]
print(li)


# In[13]:


#Basic list Operations
lst1 = [1,9,6,18,2]
print(len(lst1)) #len of the list
print(lst1*2) #repetation
print(sum(lst1))
print(9 in (lst1))
print(5 in (lst1))
print(15 in (lst1))
for x in range (len(lst1)):
    print(lst1[x])





# In[17]:


#Function of the list
lst1
a=6
print(min(lst1))
print(max(lst1))
print(sum(lst1))
print(sum(lst1)//len(lst1))
print(sum(lst1[1::2])/len(lst1[1::2]))
print((a//2))
print(lst1[1::3])


# In[21]:


# Method of the list
lst1
lst1.append(24) #Adding a new element to a list
lst1
lst1.insert(2,56) #Adding an element at particular index
lst1
lst1.count(18) #return the value how many times the object repeated
lst1.index(56) 
lst1.sort() #it sort the list in ascending order
lst1
lst1.pop() #Remove the last element of the list
lst1
lst1.pop(1) #remove an element from a particular index
lst2 = [123,23,45]
lst1.extend(lst2) #merge the list 2 into list1
lst1


# In[28]:


li = [1,9,8,2,6,3]
print(li[])

