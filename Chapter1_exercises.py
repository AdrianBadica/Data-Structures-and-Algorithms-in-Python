# -*- coding: utf-8 -*-
"""
Created on Mon Jul 20 15:47:00 2020

@author: Legion
"""

# EXERCISES CHAPTER 1

"""R-1.1 Write a short Python function, is multiple(n, m), that takes two integer
values and returns True if n is a multiple of m, that is, n = mi for some
integer i, and False otherwise."""

def is_multiple(n,m):
    if m==0 or n==0:
        print("choose a number different than zero")
    else:
        if n % m ==0 :
            return True
        else :
              return False


"""
R-1.2 Write a short Python function, is even(k), that takes an integer value and
returns True if k is even, and False otherwise. However, your function
cannot use the multiplication, modulo, or division operators.
"""



def is_even(k):
   x = list(str(k))
   if int(x[-1]) in [0,2,4,6,8]: 
       return True
   else:
       return False
   
    
   
    
"""
 R-1.3 Write a short Python function, minmax(data), that takes a sequence of
one or more numbers, and returns the smallest and largest numbers, in the
form of a tuple of length two. Do not use the built-in functions min or
max in implementing your solution.  
"""

def minmax(data):
    data.sort()
    return (data[0],data[-1])



"""
R-1.4 Write a short Python function that takes a positive integer n and returns
the sum of the squares of all the positive integers smaller than n.
"""


def sqrt_sum(n):
    sum_sqrt = 0
    while n >0:
        sum_sqrt += (n-1)**2
        n -=1
    return sum_sqrt



"""
R-1.5 Give a single command that computes the sum from Exercise R-1.4, relying
on Python’s comprehension syntax and the built-in sum function.
"""

# sum([k**2 for k in range(k)])



"""
R-1.6 Write a short Python function that takes a positive integer n and returns
the sum of the squares of all the odd positive integers smaller than n.
"""

def sqrt_odd(n):
    sum = 0
    if n < 0 : print ('n must pe positive')
    else : 
        while n>0:
            if (n-1) % 2 != 0:
                sum += (n-1)**2
                n -=1
            else:
                n -= 1
    return sum
            



"""
R-1.7 Give a single command that computes the sum from Exercise R-1.6, relying
on Python’s comprehension syntax and the built-in sum function.
"""

# sum([k**2 for k in range(k) if k % 2 !=0])




"""
R-1.8 Python allows negative integers to be used as indices into a sequence,
such as a string. If string s has length n, and expression s[k] is used for index
−n≤k<0, what is the equivalent index j ≥0 such that s[j] references
the same element?

"""

# n - k + 1





"""
R-1.9 What parameters should be sent to the range constructor, to produce a
range with values 50, 60, 70, 80?
"""

# range(50,81,10)




"""
R-1.10 What parameters should be sent to the range constructor, to produce a
range with values 8, 6, 4, 2, 0, −2, −4, −6, −8?
"""

# range(8,-9,-2)



"""
R-1.11 Demonstrate how to use Python’s list comprehension syntax to produce
the list [1, 2, 4, 8, 16, 32, 64, 128, 256].
"""

# [2**k for k in range(0,9)]



"""
R-1.12 Python’s random module includes a function choice(data) that returns a
random element from a non-empty sequence. The random module includes
a more basic function randrange, with parameterization similar to
the built-in range function, that return a random choice from the given
range. Using only the randrange function, implement your own version
of the choice function.
"""

def my_choice(data):
    import random as r
    if len(data) == 0 : print ("sequence is empty")
    else :
        return data[r.randrange(0,len(data)-1)]



"""
C-1.13 Write a pseudo-code description of a function that reverses a list of n
integers, so that the numbers are listed in the opposite order than they
were before, and compare this method to an equivalent Python function
for doing the same thing.
"""


def rev_func(data):
    l_reversed=[]
    for i in range(len(data)-1,-1,-1):
        l_reversed.append(data[i])
        i-=1
    return l_reversed


"""
C-1.14 Write a short Python function that takes a sequence of integer values and
determines if there is a distinct pair of numbers in the sequence whose
product is odd.
"""



def odd_prod(data):
    x=set()
    for i in range(len(data)):
        if len(x) == 2 : break
        if data[i] % 2 !=0: x.add(data[i])
    if len(x) == 2: print ("first two numbers who match ",x)
    else: print("no such numbers")
    
    
    
"""
C-1.15 Write a Python function that takes a sequence of numbers and determines
if all the numbers are different from each other (that is, they are distinct).
"""


def they_distinct(data):
    x = set()
    for i in range(len(data)):
        x.add(data[i])
        i+=1
    if len(data)==len(x): 
        print("all numbers are distinct")
    else: print("the numbers are not distinct")




"""
C-1.18 Demonstrate how to use Python’s list comprehension syntax to produce
the list [0, 2, 6, 12, 20, 30, 42, 56, 72, 90].

"""

[x*(x+1) for x in range(0,10)]



"""
C-1.19 Demonstrate how to use Python’s list comprehension syntax to produce
the list [ a , b , c , ..., z ], but without having to type all 26 such
characters literally.
"""

[chr(chNum) for chNum in list(range(ord('a'),ord('z')+1))]


"""
C-1.20 Python’s random module includes a function shuffle(data) that accepts a
list of elements and randomly reorders the elements so that each possible
order occurs with equal probability. The random module includes a
more basic function randint(a, b) that returns a uniformly random integer
from a to b (including both endpoints). Using only the randint function,
implement your own version of the shuffle function.
"""
def my_random(data):
    import random as r
    if len(data) in (0,1):
        return data
    for i in range(len(data)-1,0,-1):
        j = r.randint(0,i+1)
        data[i],data[j] = data[j],data[i]
    return data
 
    
"""
 C-1.21 Write a Python program that repeatedly reads lines from standard input
until an EOFError is raised, and then outputs those lines in reverse order
(a user can indicate end of input by typing ctrl-D).
"""


def read_lines():
    data = []
    try:
        while True:
            x = input("say something (CTRLD+D for end of input): ")
            data.append(x)
            print(data)
    except EOFError as e:
        data.reverse()
        print("EOFError raised, the lines in reverse order are: ",data)
        
        
        
"""
C-1.22 Write a short Python program that takes two arrays a and b of length n
storing int values, and returns the dot product of a and b. That is, it returns
an array c of length n such that c[i] = a[i] · b[i], for i = 0, . . . ,n−1.
"""

def my_dot(a,b):
    c=[0] * len(a)
    for i in range(len(a)):
        c[i]=a[i]*b[i]
    return c



"""
C-1.23 Give an example of a Python code fragment that attempts to write an element
to a list based on an index that may be out of bounds. If that index
is out of bounds, the program should catch the exception that results, and
print the following error message:
“Don’t try buffer overflow attacks in Python!”
"""
def my_dot_two(a,b):
    c=[]
    try:
        for i in range(len(a)):
            c[i]=a[i]*b[i]
            return c
    except IndexError as i : 
        print ("""Don’t try buffer overflow attacks in Python!""")
        
        
        
        
"""
C-1.24 Write a short Python function that counts the number of vowels in a given
character string.
"""

def vowels(data):
    vows=['a','e','i','o','u']
    c= 0 
    for i in range(len(data)):
        if data[i] in vows:
            c=c+1
    return c



"""
C-1.25 Write a short Python function that takes a string s, representing a sentence,
and returns a copy of the string with all punctuation removed. For example,
if given the string "Let's try, Mike.", this function would return
"Lets try Mike".
"""

def punct(s):
    p = [""",""","""'""","""."""]
    ns = []
    for i in range(len(s)):
        if s[i] not in p:
            ns.append(s[i])
    return print("".join(ns))



"""
C-1.26 Write a short program that takes as input three integers, a, b, and c, from
the console and determines if they can be used in a correct arithmetic
formula (in the given order), like “a+b = c,” “a = b−c,” or “a ∗ b = c.”
"""



def input_math():
    a = int(input("input a: "))
    b = int(input("input b: "))
    c = int(input("input c: "))
    
    if a+b == c:
        return True
    elif a == b-c:
        return True
    elif a*b == c:
        return True
    else:
        return False
    
    
    
    
    
"""
C-1.27 In Section 1.8, we provided three different implementations of a generator
that computes factors of a given integer. The third of those implementations,
from page 41, was the most efficient, but we noted that it did not
yield the factors in increasing order. Modify the generator so that it reports
factors in increasing order, while maintaining its general performance advantages.
"""

def factors(n):
    x=[]
    k=1
    while k*k <n:
        if n%k==0:
            yield k
            x.append(n // k)
        k+=1
    if k*k == n:
        yield k
    #print(x)
    x.reverse()
    for i in x:
        yield i

    
    
    
"""
Give an implementation
of a function named norm such that norm(v, p) returns the p-norm
value of v and norm(v) returns the Euclidean norm of v. You may assume
that v is a list of numbers.
"""

def p_norm(v,p=2):
    norm = 0
    for i in range(len(v)):
        norm = norm + (v[i]**p)
    norm = norm**(1/p)
    return norm
    
    
    
"""
P-1.30 Write a Python program that can take a positive integer greater than 2 as
input and write out the number of times one must repeatedly divide this
number by 2 before getting a value less than 2.
"""

def count_two():
    count = 0
    x = int(input("input your number:"))
    if x <=2 : 
        print("the number must be a postive integer greater than two")
    while x  > 2:
        count = count + 1
        x = x // 2
    return count
        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    