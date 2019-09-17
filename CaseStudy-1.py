#1-What is the output of the following code?
nums=set([1,1,2,3,3,3,4,4])
print(len(nums))

#what will be the output of the following?
d={"john":40,"peter":45}
print(list(d.keys()))
print(d.keys())
print(tuple(d.keys()))
print(list(d.values()))

#2-A website requires a user to input username and password to register.
# Write a program to check the validity of password given by user.
# Following are the criteria for checking password
username=input('please enter here username:')
password=input('please enter here password:')
# Python program to check validation of password
# Module of regular expression is used with search()
import re
password = "R@m@_f0rtu9e$"
flag = 0
while True:
    if (len(password) < 8):
        flag = -1
        break
    elif not re.search("[a-z]", password):
        flag = -1
        break
    elif not re.search("[A-Z]", password):
        flag = -1
        break
    elif not re.search("[0-9]", password):
        flag = -1
        break
    elif not re.search("[_@$]", password):
        flag = -1
        break
    elif re.search("\s", password):
        flag = -1
        break
    else:
            flag = 0
            print("Valid Password")
            break

    if flag == -1:
        print("Not a Valid Password")

#other ways
import re
p= input("Input your password")
x = True
while x:
    if (len(p)<6 or len(p)>12):
        break
    elif not re.search("[a-z]",p):
        break
    elif not re.search("[0-9]",p):
        break
    elif not re.search("[A-Z]",p):
        break
    elif not re.search("[$#@]",p):
        break
    elif re.search("\s",p):
        break
    else:
        print("Valid Password")
        x=False
        break

if x:
    print("Not a Valid Password")

#3-Write a for loop that prints all elements of a list and their position in the list.
a = [4,7,3,2,5,9]
for i in a:
    print("Element: " + str(i) + " Index: "+ str(a.index(i)))
#other ways
a = [4,7,3,2,5,9]
b = enumerate(a)
for i in b:
    print(i)

#4-Please   write   a   program   which   accepts  a   string   from   console   and   print
# the characters that have even indexes.
# Example: If the following string is given as input to the program:H1e2l3l4o5w6o7r8l9dThen,
# the output of the program should be:Helloworld

#by using slicing method
# read a string
str = input("Enter a string\n")
# create a string with characters at multiples of 2
modified_string = str[::2]
print(modified_string)

#by using while loop:
index = 0
# iterate over string
while index &lt; len(str):
    # print character at index
    print(str[index], end='')
    # increment index by 2
    index = index + 2

#by using loop:
# iterate over string
for index in range(len(str)):
    # check if index is divisible by 2
    if index % 2 == 0:
        # print character at index
        #print(str[index], end='')
         print(str[index])

# 5-Please write a program which accepts a string from console and print it in reverse order
word = input("Input a word to reverse: ")

for char in range(len(word) - 1, -1, -1):
  print(word[char], end="")
print("\n")

#other way
# Python code to reverse a string
# using extended slice syntax

# Function to reverse a string
def reverse(string):
    string = string[::-1]
    return string


s = "Geeksforgeeks"

print ("The original string  is : ", end="")
print (s)

print ("The reversed string(using extended slice syntax) is : ", end="")
print (reverse(s))

#other way
def reverse(s):
    str = ""
    for i in s:
        str = i + str
    return str


s = "Geeksforgeeks"

print ("The original string  is : ", end="")
print (s)

print ("The reversed string(using loops) is : ", end="")
print (reverse(s))

## Python code to reverse a string
# using recursion

def reverse(s):
    if len(s) == 0:
        return s
    else:
        return reverse(s[1:]) + s[0]

s = "Geeksforgeeks"

print ("The original string  is : ",end="")
print (s)

print ("The reversed string(using recursion) is : ",end="")
print (reverse(s))


# Python code to reverse a string
# using reversed()

# Function to reverse a string
def reverse(string):
    string = "".join(reversed(string))
    return string


s = "Geeksforgeeks"

print ("The original string  is : ", end="")
print (s)

print ("The reversed string(using reversed) is : ", end="")
print (reverse(s))

#6-Please write a program which count and print the numbers of each character in a string input by console
def char_frequency(str1):
    dict = {}
    for n in str1:
        keys = dict.keys()
        if n in keys:
            dict[n] += 1
        else:
            dict[n] = 1
    return dict
print(char_frequency('google.com'))

#7-With   two   given   lists   [1,3,6,78,35,55]   and   [12,24,35,24,88,120,155],
# write   a program to make a list whose elements are intersection of the above given lists.
def intersection(lst1, lst2):
    lst3 = [value for value in lst1 if value in lst2]
    return lst3


# Driver Code
lst1 = [4, 9, 1, 17, 11, 26, 28, 54, 69]
lst2 = [9, 9, 74, 21, 45, 11, 63, 28, 26]
print(intersection(lst1, lst2))

#8-With a given list [12,24,35,24,88,120,155,88,120,155],
# write a program to print this list after removing all duplicate values with original order reserved.
a = [12,24,35,24,88,120,155,88,120,155]

dup_items = set()
uniq_items = []
for x in a:
    if x not in dup_items:
        uniq_items.append(x)
        dup_items.add(x)

print(dup_items)

#By using list comprehension,
#9- please write a program to print the list after removing the value 24 in [12,24,35,24,88,120,155].
numbers = [12,24,35,24,88,120,155]
numbers = [x for (i,x) in enumerate(numbers) if i not in (1,3)]
print(numbers)

#By using list comprehension,
#-10 please write a program to print the list after removing the 0th,4th,5th numbers in [12,24,35,70,88,120,155]
color = [12,24,35,70,88,120,155]
color = [x for (i,x) in enumerate(color) if i not in (0,4,5)]
print(color)

#-11 By using list comprehension,
# please write a program to print the list after removing delete numbers
# which are divisible by 5 and 7 in [12,24,35,70,88,120,155]
lst = [12,24,35,70,88,120,155]
lst = [x for x in lst if x%5!=0 and x%7!=0]
print lst # [12, 24, 88]

#-12 Please  write  a  program  to  randomly  generate  a  list  with  5  numbers,
# which  are divisible by 5 and 7 , between 1 and 1000 inclusive.
count = 0
for i in range(1,1001):
    if i%3 and i%5 and i%7:
        count += 1
print(count)

import random
print random.sample(range(1,1000), 5)

import random
print random.sample([i for i in range(1,1001) if i%5==0 and i%7==0], 5)

#-13 Write  a  program  to  compute  1/2+2/3+3/4+...+n/n+1  with  a  given  n  input  by console (n>0)
def sum(n):
    i = 1
    s = 0.0
    for i in range(1, n + 1):
        s = s + 1 / i;
    return s;
# Driver Code
n = 5
print("Sum is", round(sum(n), 6))

