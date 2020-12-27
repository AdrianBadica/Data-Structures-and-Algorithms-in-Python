# -*- coding: utf-8 -*-
"""
Created on Sat Dec 26 18:33:10 2020

@author: Legion
"""

"""
R-6.3 Implement a function with signature transfer(S, T) that transfers all elements
from stack S onto stack T, so that the element that starts at the top
of S is the first to be inserted onto T, and the element at the bottom of S
ends up at the top of T.
"""

def transfer(S,T):
    while not S.is_empty():
        T.push(S.pop())
    
    
"""R-6.4 Give a recursive method for removing 
all the elements from a stack."""



def rec_rem(S):
    if S.is_empty():
        print("end of stack")
    else:
        S.pop()
        rec_rem(S)



"""R-6.5 Implement a function that reverses a list of elements by pushing them onto
a stack in one order, and writing them back to the list in reversed order."""

def rev_list(L):
    S=ArrayStack()
    for i in range(len(L)):
        S.push(L[i])
    L = []
    while not S.is_empty():
        L.append(S.pop())
    return L



     

"""R-6.13 Suppose you have a deque D containing the numbers (1,2,3,4,5,6,7,8),
in this order. Suppose further that you have an initially empty queue Q.
Give a code fragment that uses only D and Q (and no other variables) and
results in D storing the elements in the order (1,2,3,5,4,6,7,8)."""

Q.enqueue(D.delete_last()) # add 8 to queue
Q.enqueue(D.delete_last()) # add 7 to queue
Q.enqueue(D.delete_last()) # add 6 to queue


D.add_first(D.delete_last()) # move 5 from the end of the deque to the start

Q.enqueue(D.delete_last()) # add 4 to queue

Q.enqueue(D.delete_first()) # add 5 to queue

Q.enqueue(D.delete_last()) # add 3 to queue
Q.enqueue(D.delete_last()) # add 2 to queue
Q.enqueue(D.delete_last()) # add 1 to queue
        
