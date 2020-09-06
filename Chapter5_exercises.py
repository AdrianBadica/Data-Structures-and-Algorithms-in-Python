# -*- coding: utf-8 -*-
"""
Created on Sun Aug 30 13:12:52 2020

@author: Legion
"""

"""R-5.4 Our DynamicArray class, as given in Code Fragment 5.3, does not support
use of negative indices with getitem . Update that method to better
match the semantics of a Python list."""


import ctypes
class DynamicArray:
    
    def __init__(self):
        self._n=0
        self._capacity=1
        self._A=self._make_array(self._capacity)
        
    def __len__(self):
        return self._n
    
    def __getitem__(self,k):
        if k>=0 and k<self._n:
            return self._A[k]
        elif k<0 and  abs(k)<=self._n:
            return self._A[self._n+k]
        else:
            raise IndexError('invalid index')
    
    def append(self,obj):
        if self._n==self._capacity:
            self._resize(2*self._capacity)
        self._A[self._n] =obj
        self._n+=1
        
    def _resize(self,c):
        B=self._make_array(c)
        for k in range(self._n):
            B[k]=self._A[k]
        self._A=B
        self._capacity=c
        
        
    def insert(self,k,value):
        if self._n==self._capacity:
            self._resize(2*self._capacity)
        for j in range(self._n,k,-1):
            self._A[j]=self._A[j-1]
            self._A[k]=value
            self._n+=1
        
    def _make_array(self,c):
        return (c*ctypes.py_object)()
    
    






"""
R-5.11 Use standard control structures to compute the sum of all numbers in an
n×n data set, represented as a list of lists.
"""
 
def all_sum(S):
    all_sum=0
    for j in range(len(S)):
        for i in range (len(S[j])):
            all_sum = all_sum + S[j][i]
    return all_sum




"""
C-5.14 The shuffle method, supported by the random module, takes a Python
list and rearranges it so that every possible ordering is equally likely.
Implement your own version of such a function. You may rely on the
randrange(n) function of the random module, which returns a random
number between 0 and n−1 inclusive.
"""


def my_shuffle(a):
    import random as r
    n=len(a)
    x=[]
    for i in range (10*n):
        z = r.randrange(n)
        if z not in x: x.append(z)
    a=[a[i] for i in x]
    return a








"""
C-5.25 The syntax data.remove(value) for Python list data removes only the first
occurrence of element value from the list. Give an implementation of a
function, with signature remove all(data, value), that removes all occurrences
of value from the given list, such that the worst-case running time
of the function is O(n) on a list with n elements. Not that it is not efficient
enough in general to rely on repeated calls to remove.
"""

def remove_all(data,value):
    x=[]
    for i in range(len(data)):
        if data[i] != value:
            x.append(data[i])
    a=x
    return a
    
    
    