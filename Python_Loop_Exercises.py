#!/usr/bin/env python
# coding: utf-8

# # Exercise 1: Print First 10 natural numbers using while loop

# In[4]:


for i in range(1,11):
    print(i)


# # Exercise 2: Print the following pattern

# ![image.png](attachment:image.png)

# In[8]:


n = 5
for i in range(1, n+1):
    for j in range(1, i+1):
        print(j, end=" ")
    print("\n")


# # Exercise 3: Calculate the sum of all numbers from 1 to a given number

# In[5]:


s = 0
n = int(input("Enter number "))
for i in range(n + 1):
    s += i
print("\n")
print("Sum is: ", s)


# # Exercise 4: Write a program to print multiplication table of a given number

# In[4]:


n = int(input("Enter the number: "))
for i in range(1,11):
    print(n*i)


# # Exercise 5: Display numbers from a list using loop
# numbers = [12, 75, 150, 180, 145, 525, 50]
# 
# Write a program to display only those numbers from a list that satisfy the following conditions.
# 1) The number must be divisible by five.
# 2) If the number is greater than 150, then skip it and move to the next number.
# 3) If the number is greater than 500, then stop the loop.

# In[15]:


numbers = [12, 75, 150, 180, 145, 525, 50]

for i in numbers:
    if i>500:
        break
    if i>150:
        continue
    elif i%5==0:
        print(i)


# # Exercise 6: Count the total number of digits in a number

# In[16]:


num = int(input("Enter numbers: "))
count = 0
while num != 0:
    num = num//10
    count += 1
print("Total digits: ", count)


# # Exercise 7: Print the following pattern
# ![image.png](attachment:image.png)

# In[20]:


n = 5
k = 5
for i in range(0,n+1):
    for j in range(k-i,0,-1):
        print(j,end=' ')
    print()


# # Exercise 8: Print list in reverse order using a loop
# 
# list1 = [10, 20, 30, 40, 50]

# In[24]:


list1 = [10, 20, 30, 40, 50]

revlist1 = reversed(list1)

for i in  revlist1:
    print(i)


# # Exercise 9: Display numbers from -10 to -1 using for loop

# In[3]:


for i in range(-10, 0):
    print(i)


# # Exercise 10: Use else block to display a message “Done” after successful execution of for loop
# 
# ![image.png](attachment:image.png)
# 

# In[5]:


#given

for i in range(5):
    print(i)
else:
    print("Done!")


# #  Exercise 11: Write a program to display all prime numbers within a range
# Given:
# start = 25
# end = 50

# In[6]:


start = 25
end = 50
print("Prime numbers between", start, "and", end, "are:")

for num in range(start, end + 1):
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                break
        else:
            print(num)


# # Exercise 12: Reverse a given integer number
# 
# Given: 76542

# In[3]:


num = 76542
reverse_number = 0
print("Given Number ", num)
while num > 0:
    reminder = num % 10
    reverse_number = (reverse_number * 10) + reminder
    num = num // 10
print("Revere Number ", reverse_number)


# # Exercise 13: Print the following pattern
# 
# ![image.png](attachment:image.png)

# In[6]:


rows = 5
for i in range(0, rows):
    for j in range(0, i + 1):
        print("*", end=' ')
    print("\r")

for i in range(rows, 0, -1):
    for j in range(0, i - 1):
        print("*", end=' ')
    print("\r")

