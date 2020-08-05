# -*- coding: utf-8 -*-
"""
Created on Sat Aug  1 14:13:10 2020

@author: Legion
"""

"""
R-2.4 Write a Python class, Flower, that has three instance variables of type str,
int, and float, that respectively represent the name of the flower, its number
of petals, and its price. Your class must include a constructor method
that initializes each variable to an appropriate value, and your class should
include methods for setting the value of each type, and retrieving the value
of each type.
"""

class Flower:
    def __init__(self, name = str, petals = int,price = float):
        self._name=name
        self._petals=petals
        self._price=price
        
    def get_name(self):
        return self._name
    def get_petals(self):
        return self._petals
    def get_price(self):
        return self._price
    
    def set_name(self, val):
        self._name = val
    def set_petals(self, val):
        self._petals = val
    def set_price(self, val):
        self._price = val
    
    
"""
R-2.5 Use the techniques of Section 1.7 to revise the charge and make payment
methods of the CreditCard class to ensure that the caller sends a number
as a parameter.
"""


class CreditCard:
    """ a consumer credit card"""
    
    def __init__(self, customer,bank,acnt,limit):
        
        self._customer = customer
        self._bank=bank
        self._account= acnt
        self._limit=limit
        self._balance=0
        
    def get_customer(self):
        return self._customer
    
    def get_bank(self):
        return self._bank
    
    def get_account(self):
        return self._account
    
    def get_limit(self):
        return self._limit
    
    def get_balance(self):
        return self._balance
    
    def charge(self,price):
        if not type(price) in (int,float):
            raise TypeError("Price should be a number")
        if price + self._balance > self._limit:
            return False
        else:
            self._balance+=price
            return True
        
    def make_payment(self,amount):
        if not type(amount) in (int,float):
            raise TypeError("Amount should be a number")
        self._balance -=amount
        
"""
R-2.6 If the parameter to the make payment method of the CreditCard class
were a negative number, that would have the effect of raising the balance
on the account. Revise the implementation so that it raises a ValueError if
a negative value is sent.
"""
class CreditCard_R26:
    """ a consumer credit card"""
    
    def __init__(self, customer,bank,acnt,limit):
        
        self._customer = customer
        self._bank=bank
        self._account= acnt
        self._limit=limit
        self._balance=0
        
    def get_customer(self):
        return self._customer
    
    def get_bank(self):
        return self._bank
    
    def get_account(self):
        return self._account
    
    def get_limit(self):
        return self._limit
    
    def get_balance(self):
        return self._balance
    
    def charge(self,price):
        if not type(price) in (int,float):
            raise TypeError("Price should be a number")
        if price + self._balance > self._limit:
            return False
        else:
            self._balance+=price
            return True
        
    def make_payment(self,amount):
        if not type(amount) in (int,float):
            raise TypeError("Amount should be a number")
        if amount < 0:
            raise ValueError('Amount should be a positive number')
        self._balance -=amount
        
"""
R-2.7 The CreditCard class of Section 2.3 initializes the balance of a new account
to zero. Modify that class so that a new account can be given a
nonzero balance using an optional fifth parameter to the constructor. The
four-parameter constructor syntax should continue to produce an account
with zero balance.
"""

class CreditCard_R27:
    """ a consumer credit card"""
    
    def __init__(self, customer,bank,acnt,limit,balance=0):
        
        self._customer = customer
        self._bank=bank
        self._account= acnt
        self._limit=limit
        self._balance=balance
        
    def get_customer(self):
        return self._customer
    
    def get_bank(self):
        return self._bank
    
    def get_account(self):
        return self._account
    
    def get_limit(self):
        return self._limit
    
    def get_balance(self):
        return self._balance
    
    def charge(self,price):
        if not type(price) in (int,float):
            raise TypeError("Price should be a number")
        if price + self._balance > self._limit:
            return False
        else:
            self._balance+=price
            return True
        
    def make_payment(self,amount):
        if not type(amount) in (int,float):
            raise TypeError("Amount should be a number")
        if amount < 0:
            raise ValueError('Amount should be a positive number')
        self._balance -=amount


"""
R-2.9 Implement the sub method for the Vector class of Section 2.3.3, so
that the expression u−v returns a new vector instance representing the
difference between two vectors.
"""

class Vector:
    
    def __init__(self,d):
        if type(d) == int:
            self._coords=[0]*d
        else:
            self._coords=[0]*len(d)
            for i in range(len(d)):
                self._coords[i]=d[i]
        
    def __len__(self):
        return len(self._coords)
    
    def __getitem__(self,j):
        return (self._coords[j])
    
    def __setitem__(self,j,val):
        self._coords[j]= val
        
    def __radd__(self,other):
        if len(self) != len (other):
            raise ValueError ('dimensions must match')
        result = Vector(len(self))
        for j in range(len(self)):
            result[j] = self[j]+other[j]
        return result
    
    def __add__(self,other):
        if len(self) != len (other):
            raise ValueError ('dimensions must match')
        result = Vector(len(self))
        for j in range(len(self)):
            result[j] = self[j]+other[j]
        return result
    
    
    def __sub__(self,other):
        if len(self) != len (other):
            raise ValueError ('dimensions must match')
        result = Vector(len(self))
        for j in range(len(self)):
            result[j] = self[j]-other[j]
        return result
    
            
    def __eq__ (self,other):
        return self._coords==other._coords
    
    def __ne__(self,other):
        return not self == other
    
    def __str__(self):
        return '<' + str(self._coords)[1:-1]+'>'
    
    
    def __neg__(self):
        result=Vector(len(self))
        for j in range(len(self)):
            result[j]=0-self[j]
        return result
    
    # def __mul__(self,val):
    #     result = Vector(len(self))
    #     for j in range(len(self)):
    #         result[j] = self[j]*val
    #     return result
    
    def __rmul__(self,val):
        result = Vector(len(self))
        for j in range(len(self)):
            result[j] = self[j]*val
        return result
    
    # def __mul__(self,other):
    #     if len(self) != len (other):
    #         raise ValueError ('dimensions must match')
    #     result = 0
    #     for j in range(len(self)):
    #         result = result + self[j]*other[j]
    #     return result
    
    def __mul__(self,other):
        if type(other)==int:
            result = Vector(len(self))
            for j in range(len(self)):
                result[j] = self[j]*other
            return result
        else:
            if len(self) != len (other):
                raise ValueError ('dimensions must match')
            result = 0
            for j in range(len(self)):
                result = result + self[j]*other[j]
            return result
            
            
    
"""
R-2.10 Implement the neg method for the Vector class of Section 2.3.3, so
that the expression −v returns a new vector instance whose coordinates
are all the negated values of the respective coordinates of v.
"""

### see above





"""
104 Chapter 2. Object-Oriented Programming
R-2.11 In Section 2.3.3, we note that our Vector class supports a syntax such as
v = u + [5, 3, 10, −2, 1], in which the sum of a vector and list returns
a new vector. However, the syntax v = [5, 3, 10, −2, 1] + u is illegal.
Explain how the Vector class definition can be revised so that this syntax
generates a new vector.
"""

### added __radd__


"""
R-2.12 Implement the mul method for the Vector class of Section 2.3.3, so
that the expression v 3 returns a new vector with coordinates that are 3
times the respective coordinates of v.
"""

### added __mul__




"""
R-2.13 Exercise R-2.12 asks for an implementation of mul , for the Vector
class of Section 2.3.3, to provide support for the syntax v 3. Implement
the rmul method, to provide additional support for syntax 3 v.
"""

### added __rmul__


"""

R-2.14 Implement the mul method for the Vector class of Section 2.3.3, so
that the expression u v returns a scalar that represents the dot product of
the vectors.
"""


### changed mul



"""
R-2.15 The Vector class of Section 2.3.3 provides a constructor that takes an integer
d, and produces a d-dimensional vector with all coordinates equal to
0. Another convenient form for creating a new vector would be to send the
constructor a parameter that is some iterable type representing a sequence
of numbers, and to create a vector with dimension equal to the length of
that sequence and coordinates equal to the sequence values. For example,
Vector([4, 7, 5]) would produce a three-dimensional vector with coordinates
<4, 7, 5>. Modify the constructor so that either of these forms is
acceptable; that is, if a single integer is sent, it produces a vector of that
dimension with all zeros, but if a sequence of numbers is provided, it produces
a vector with coordinates based on that sequence.
"""

###  done, see above


"""
R-2.18 Give a short fragment of Python code that uses the progression classes
from Section 2.4.2 to find the 8th value of a Fibonacci progression that
starts with 2 and 2 as its first two values.
"""


class Progression:
    def __init__(self,start=0):
        self._current=start
    def _advance(self):
        self._current+=1
    def __next__(self):
        if self._current is None:
            raise StopIteration()
        else:
            answer = self._current
            self._advance()
            return answer
    def __iter__(self):
        return self
    def print_progression(self,n):
        print(' '.join(str(next(self)) for j in range(n)))
    
 
            
        
        
        
class Fibo(Progression):
    def __init__(self,first=0,second=1):
        super().__init__(first)
        self._prev = second-first
    def _advance(self):
        self._prev,self._current=self._current,self._prev+self._current
    ### answer
    def get_item(self,n):
        result=[]
        for j in range(n):
            result.append(next(self))
        return result[n-1]

### x= Fibo(2,2)
### x.get_item(8)
### 42


"""
R-2.22 The collections.Sequence abstract base class does not provide support for
comparing two sequences to each other. Modify our Sequence class from
Code Fragment 2.14 to include a definition for the eq method, so
that expression seq1 == seq2 will return True precisely when the two
sequences are element by element equivalent.
"""





from abc import ABCMeta, abstractmethod

class Sequence(metaclass=ABCMeta):
    @abstractmethod 
    def __len__(self):
        """"""
    @abstractmethod 
    def __getitem__(self,j):
        """"""   
    def __contains__(self,val):
        for j in range(len(self)):
            if slef[j]==val:
                return True
        return False
    
    def index(self,val):
        for j in range(len(self)):
            if self[j]==val:
                return j
        raise ValueError('value not in sequence')
        
    def count(self,val):
        k=0
        for j in range(len(self)):
            if self[j]==val:
                k+=1
        return k
    
    def __eq__(self,other):
        if len(self) != len (other):
            raise ValueError ('dimensions must match')
        result = 0
        for j in range(len(self)):
            if self[j]==other[j]:
                result +=1
        if result == len(self):
            return True
        else:
            return False

    
    def __lt__(self,other):
        if len(self) != len (other):
            raise ValueError ('dimensions must match')
        result = 0
        for j in range(len(self)):
            if self[j]<other[j]:
                result +=1
        if result == len(self):
            return True
        else:
            return False

"""
R-2.23 In similar spirit to the previous problem, augment the Sequence class with
method lt , to support lexicographic comparison seq1 < seq2.
"""



### added __lt__ above



"""
C-2.25 Exercise R-2.12 uses the mul method to support multiplying a Vector
by a number, while Exercise R-2.14 uses the mul method to support
computing a dot product of two vectors. Give a single implementation of
Vector. mul that uses run-time type checking to support both syntaxes
u v and u k, where u and v designate vector instances and k represents
a number.
"""


    # def __mul__(self,other):
    #     if type(other)==int:
    #         result = Vector(len(self))
    #         for j in range(len(self)):
    #             result[j] = self[j]*other
    #         return result
    #     else:
    #         if len(self) != len (other):
    #             raise ValueError ('dimensions must match')
    #         result = 0
    #         for j in range(len(self)):
    #             result = result + self[j]*other[j]
    #         return result






"""
C-2.26 The SequenceIterator class of Section 2.3.4 provides what is known as a
forward iterator. Implement a class named ReversedSequenceIterator that
serves as a reverse iterator for any Python sequence type. The first call to
next should return the last element of the sequence, the second call to next
should return the second-to-last element, and so forth.
"""



class SequenceIteratorReversed:
    
    def __init__(self,sequence):
        self._seq=sequence
        self._k=len(self._seq)
        
    def __next__(self):
        self._k-=1
        if self._k>-1:
            return (self._seq[self._k])
        else:
            raise StopIteration()
            
    def __iter__(self):
        return self



"""
C-2.27 In Section 2.3.5, we note that our version of the Range class has implicit
support for iteration, due to its explicit support of both len
and getitem . The class also receives implicit support of the Boolean
test, “k in r” for Range r. This test is evaluated based on a forward iteration
through the range, as evidenced by the relative quickness of the test
2 in Range(10000000) versus 9999999 in Range(10000000). Provide a
more efficient implementation of the contains method to determine
whether a particular value lies within a given range. The running time of
your method should be independent of the length of the range.
"""

class Range:
    def __init__(self,start,stop=None,step=1):
        if step==0:
            raise ValueError('step cannot be 0')
        if stop is None:
            start,stop=0,start
        self._length=max(0,(stop-start+step-1)//step)
        self._start=start
        self._step=step
    
    def __len__(self):
        return self._length
    
    def __getitem__(self,k):
        if k<0:
            k+=len(self)
        if not 0<=k<self._length:
            raise IndexError('index out of range')
        return self._start+k*self._step
    
    def in_range(self,val):
        if (self._start <=val) & (val%self._step ==0):
            return True
        else:
            return False



"""
C-2.28 The PredatoryCreditCard class of Section 2.4.1 provides a process month
method that models the completion of a monthly cycle. Modify the class
so that once a customer has made ten calls to charge in the current month,
each additional call to that function results in an additional $1 surcharge.
"""

class PredatoryCreditCard(CreditCard):
    def __init__(self, customer,bank,acnt,limit,apr):
        super().__init__(customer,bank,acnt,limit)
        self._apr=apr
    def charge(self,price, z=0,c=[]):
        success=super().charge(price)
        if not success:
            self._balance+=5
        c.append(1)
        self._z=len(c)
        return success
    def process_month(self):
        if self._z >= 10:
            if self._balance > 0 :
                monthly_factor = pow(1+self._apr,1/12)
                self._balance+= (monthly_factor+self._z)
        else:
            if self._balance > 0 :
                monthly_factor = pow(1+self._apr,1/12)
                self._balance+= monthly_factor
        print(self._balance, self._z)
 
                





