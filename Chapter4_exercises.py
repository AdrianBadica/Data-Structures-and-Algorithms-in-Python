"""
C-4.9 Write a short recursive Python function that finds the minimum and maximum values
in a sequence without using any loops.
"""

def min_max(data):
	n=len(data)
	res=[]
	res2=[]
	if n==1:
		return [data[0],data[0]]
	else:
		mid = n//2
		res=min_max(data[:mid])
		res2=min_max(data[mid:])
		if (res2[0]<res[0]):
			res[0]=res2[0]
		if (res2[1]>res[1]):
			res[1]=res2[1]
		return res


"""
C-4.12 Give a recursive algorithm to compute the product of two positive integers,
m and n, using only addition and subtraction.
"""

def product(m,n):
    if m==1:
        return n
    elif n==1:
        return m
    else:
        return n + product(n,m-1)

    
"""
C-4.15 Write a recursive function that will output all the subsets of a set of n
elements (without repeating any subsets).
"""


def my_set(string,index,current):
    if index==len(string):
        print(current)
        return
    my_set(string,index+1,current + string[index])
    my_set(string,index+1,current)



"""
C-4.16 Write a short recursive Python function that takes a character string s and
outputs its reverse. For example, the reverse of pots&pans would be
snap&stop .
"""

def rev(S):
    if S=="":
        return S
    else:
        return S[-1]+rev(S[:-1])

"""
C-4.17 Write a short recursive Python function that determines if a string s is a
palindrome, that is, it is equal to its reverse. For example, racecar and
gohangasalamiimalasagnahog are palindromes.
"""


def pal(S):
    if len(S)<2:
        return True
    if S[0] != S[-1]:
        return False
    return pal(S[1:-1])
    





        
                

        
