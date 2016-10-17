# -*- coding: utf-8 -*-
"""
Created on Thu Sep 22 17:42:28 2016

@author: Tshark
"""

# -*- coding: utf-8 -*-
"""
Created on Thu Sep 15 18:49:44 2016

@author: Tshark
"""
'''
Problem 1
This function returns the nth Fibonacc using recrusion and tells us
what index of Fibonacc number has 100 digits 

'''


def fibnum(num):
    """
    This function returns the nth Fibonacc number using 1 as the first Fib number
    """
    if num ==1:       #The first Fib number is 1
        return 1
    else:               #if not the first number, use recrusion here to use the previous two to fib numbers to calculate the next 
        answer = fibnum(num-1) + fibnum(num-2)
        return answer
        
                  
stop = False               #While loop search variable

numlist = [1, 2]            #list out the second and thrid Fib numbers 
counter = 4                 #starting index of the next Fib numbers in the list

"""
This while loop checks for the fib numbers that contains 100 digits, if the nunber doesn't have 100 digits
update this number to the second item in the list and move the previous second number to first number
"""
while stop == False:
    newnum = numlist[0]+numlist[1]
    if(len(str(newnum))) >= 100:    #convert num to str and check to see if the digits > 100
        print("the index of the 100 digit Fib number is: ", counter)              #print out the fib index
        print("The Fib number is : ", newnum)               #print out the fib num
        stop = True
    else:
        numlist[0] = numlist[1]
        numlist[1] = newnum
        counter += 1

#-------------------------------------------------------------------------------------------------------------------------

# -*- coding: utf-8 -*-
"""
Created on Thu Sep 17 18:49:44 2016

@author: TCheng
"""

'''
Problem 2
This programming find the maximum total from top to bottom of the number triangle
without using recrusion
'''



tree = [[75],
        [95, 64],
        [17, 47, 82],
        [18, 35, 87, 10],
        [20,  4, 82, 47, 65],
        [19,  1, 23, 75,  3, 34],
        [88,  2, 77, 73,  7, 63, 67],
        [99, 65,  4, 28,  6, 16, 70, 92],
        [41, 41, 26, 56, 83, 40, 80, 70, 33], 
        [41, 48, 72, 33, 47, 32, 37, 16, 94, 29],
        [53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14],
        [70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57],
        [91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48],
        [63, 66,  4, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31],
        [ 4, 62, 98, 27, 23,  9, 70, 98, 73, 93, 38, 53, 60,  4, 23]]




def solve():
    """
    The function uses dynamic programming to solve. First, we break down the big problems into
    smaller problems. We starts from the second bottom row of the tree. Each number on that row has 
    two adjacent numbers below in the row below. The algorithms take the sum of the maximum value of 
    current iterated numbers and the below adjacent numbers. This continues til it hits the index[0][0],
    which is the top of the tree and it maximum sum of path will be calculated. 
    
    """
    
    for row in range(len(tree)-1, 0, -1):       #recusive the for loop solving from bottom first
        for col in range(0, row):               
            tree[row-1][col] += max(tree[row][col], tree[row][col+1])  # add the maximum adjacent value of the row below 
    return tree[0][0]        
    
    
print(solve())

#-------------------------------------------------------------------------------------------------------------------------

# -*- coding: utf-8 -*-
"""
Created on Thu Sep 22 15:49:40 2016

@author: Tshark
"""

"""
Problem3
    This function runs the Collatz chain for starting value
    n, under these conditions if n is even, n → n/2, if n is odd, n → 3n + 1.
    For instance, if we use the rule above and starting with 13, we generate the following sequence:
    13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1 It can be seen that this sequence (starting at 13 and
    finishing at 1) contains 10 terms. This program finds the longest Collatz chain with an integer under 1000.
"""


def collatz(n):
    """
    the function calculates the length of the Collatz chain for a given integer
    parameters:
    n: a positive integer
    return: the length of collatz chain
    """
    i=1     #counter of the chain
    while n!=1:  #This while loop ends when the number is 1
        if n%2==0:
            n=n/2       #if n is even
        else:
            n=3*n+1     #if n is odd
        i=i+1           # counter of the length chain
    return i
    
    
def main():
    """
    This is the main function and it finds the integer with max length of chain 
    """
    t=collatz(1) #initalize the biggest number as collatz(1) and update this number as the iteration goes 
    j=1 # initalize the index of biggest number of collatz()
    for i in range(1,1000):     #this loop goes checks the number from 1 to 1000
        if t<collatz(i):    
            t=collatz(i)  #update the legnth of chain
            j=i         #update the number 
        else:
            continue
    print('the number', j, 'has longest chain with chain length:', t)
main()

#-------------------------------------------------------------------------------------------------------------------------
"""
Created on Thu Sep 22 13:52:54 2016

@author: TCheng
"""
#Stuart- Interesting solution and correct, but if you wanted to run this program 
#on integers greater than 2000 your code would fail. If you decided not to call 
#any external lbiraries you could try implementing long division from scratch, but
#this solves the problem as asked.

from decimal import *
getcontext().prec = 2000 #set longer decimal place for calculation
def recur_cycle(value):
    """
    the function calculates the length of the recurring cycle for the reciporal of 
    an integer in the decimal representation. Then it finds the number that produces the 
    longest length
    
    parameters:
    value: is a arbitary number
    
    return :the length of recurring cycle
    """
    tem = Decimal(1)/Decimal(value) #get the decimal numbers
    deci=list(str(tem)) #trasfer the decimal to a list for convenient of later comparison
    if len(deci)<999:
        return 0 # check to see if the decimal places is finite, if so the length of recursion cycle is 0
    else:
        n=1 #counter of the length
        while True:    
            if deci[10]==deci[10+n]: #compare value from 10th term because some cycles are not start from beginning, so we define the start from 10th value, if some value is same as the start, turn into next comparison 
                z=1 # z is a stop indicator, if n is cycle length, then z=1, otherwise z=0
                for i in range(0,n):    #checks the value from the previous digits to see if they cycles
                    if deci[10+i]==deci[10+n+i]:# if one value is the same at the beginning, then compare the every values after that position
                        continue
                    else:
                        z=0 # if z =0, n is not cycle length
                        break
                if z==1:
                    return n  #if z =1, the range up to n is a cycle, the return the cycle length n
                else:
                    n=n+1 # if n is not cycle length, increment n to check for recurring cycle 
                    continue
            else:   
                n=n+1
                continue
            
def main():
    '''
    Use the function, recur_cycle(), to find the value of d < 500 for which 1/d 
    contains the longest recurring cycle in its decimal fraction part
    '''
    value=2
    max=recur_cycle(1)   #initialize the max length 1
    for i in range(2,500): #checks the number from 2 to 500
        if recur_cycle(i)>max:  # if current length of the cycle is longer than max, update it as max
            max=recur_cycle(i) 
            value=i         #store the length in the variable value
        else:
            continue            
    print('the number', value, 'have the longest recurring cycle with cycle length: ',max) #max is the maximum length of recursion cycle and 'value' is its corresponding value
main()




#-------------------------------------------------------------------------------------------------------------------------

'''Created on Thu Sep 22 15:49:40 2016

@author: TCheng
'''
import numpy

#Stuart- Excellent solution, very fast. Numpy is very powerfulv(fast) when needing to 
#do heavy mathematical coding.

"""
Problem 5
This function calculates the number of ways to make change for a given value of pounds.
The algorithm uses dynamic programming in order to break the large problem down
into smaller problems by solving from the bottom. for instance, it solves for how many
combinations it can make for 10p with a specific amounts of 1p, a combination of 1p, 2p and 5p, etc.
Then the algorithm uses the stored value for previous combination to find the desired exchange
The algorithm creates a matrix and stores all the previous calculated values.
Parameters:
pence : total change to give, in pence.
"""


def make_change(pence):
    target = pence # target amount of change to make
    coins = [1, 2, 5, 10, 20, 50, 100, 200] # The list of available coin denominations with which to make change
    combinations = numpy.zeros((target+1, len(coins))) #create 201 x 8 matrices with zeros
    for i in range(0, target +1):
        combinations[i][0] = 1 #there is only one way to make N pence with 1p coins

    for j in range(0, target + 1):          #going down the row of the matrix
        for k in range(1, len(coins)):      #going though the columun matrix
            if j >= coins[k]:
                combinations[j][k] += combinations[j][k-1] # number of ways to form current target with only coin values less than coins[k]
                combinations[j][k] += combinations[j-coins[k]][k] # plus number of ways to form current target using coin values equal to coins[k]
            else:
                combinations[j][k] = combinations[j][k-1] # if less than current coin value, the value is the same as the left cell

    print('There are {0} ways to make change for {1} pence.'.format(combinations[target][len(coins)-1], target))

make_change(200)

#-------------------------------------------------------------------------------------------------------------------------

# -*- coding: utf-8 -*-
"""
Created on Thu Sep 22 10:23:08 2016

@author: TCheng
"""
'''
Problem 6
This program prompts user for an input of an integer and determines
whether it is a prime number 

'''

import math

#Stuart- While yes this does determine if a number is prime this is not a recursive program.
#Remember recursive programs are ones that call for the running of themselves inside their code.

def prime(n):
    """
    #This function takes an integer as input, returns True if it's a prime, 
    returns False if it is not. 
    Parameters
    n = number input by user, assume a positive integer
    """

    if n >1:  # check that number is greater than 1
        if n == 2:
            return True  
        elif n % 2 == 0:  # if the number is even
            return False  
        else: 
        # the sqrt takes care of the the number 
        # This for loop takes care of the number that is not division by 2 but odd numbers after 1
            for i in range(3, int(math.sqrt(n))+1, 2):
                if n % i == 0:
                    return False  # number is not prime if it has factors that is smaller than number
                else:
                    return True  
            return False  
    


num = input("Enter a positive integer: ")
num = int(num)
if prime(num) == True:
    print(num, "is a prime number")
else:
    print(num, "is not a prime number")
    
#-------------------------------------------------------------------------------------------------------------------------
    # -*- coding: utf-8 -*-
"""
Created on Thu Sep 22 13:52:54 2016

@author: TCheng
"""

"""
This program  accepts a list of strings and uses recursion to return a sorted list. Each step should at
most modify two elements of the list.
"""

#Stuart- Well written example of recursion, good job.

def sort(lst, offset = None):
    """
    the sort function is the main function using recrusion to return the current sorted list
    to next iteration til the list is completely sorted
    NOT: this is sorted based on the order of ASCIII code of character    
    
    parameters: 
    lst = list of random string
    offset = variable of stop condition of recruisve loop
    """

    if(offset is None):  # set the offset to the last index of lst
        offset = len(lst)-1
	
# checking for the base case of the recursion. i.e, to stop iterating when offset has reached 0(which means the list is sorted)
    if(offset >= 0):
        lst = sort(lst, offset-1)   # recursive step
        ele = offset  # set the value of ele to the offset, we assume this to be the smallest element

        # for loop to find the smallest element in range (offset, len(lst))
        for i in range(offset + 1, len(lst)) :
        # change the smallest element index i.e. ele , if smaller element is encountered
            if(lst[ele] > lst[i]) :
                ele = i

		# swap the element at offset with that at ele
        temp = lst[offset]
        lst[offset] = lst[ele]
        lst[ele] = temp

		# print the current list
    print("\n\nstep " + str(offset + 1) + " : ")
    for i in range(0, len(lst)) :
        print(lst[i])

    return lst


data = ["jim", "Jim", "apple", "girl", "fRiend", "1", "+", "T", "!"]
sort(data)

#-------------------------------------------------------------------------------------------------------------------------

# -*- coding: utf-8 -*-
"""
Created on Thu Sep 22 10:23:08 2016

@author: Tshark
"""
'''
Question 8: This program prompts user for an input of an integer and determines
whether it is a prime number 

'''

def fun1(x,n):
    """
    the function calculates the value of f(x)=3.95*（x-x**2）with n times recursion
    parameters:
    x: a number in [0,1] 
    n: numbers of recursion 
    """
    
    if n==1:        #if n=1, return base case
        return 3.95*(x-x**2) 
    else:
        return fun1(fun1(x,1),n-1) # if n!= 1, then take the value from previous iteration into the next iteration

def fun2(x,n):
    """
    the function calculuates the value function f(x)=3.95*x*(1-x）through n times recursion
    
    parameters:
    x: a number in [0,1] 
    n: number of recursion 
    """
    if n==1:     #if n=1, return base case
        return 3.95*x*(1-x) 
    else:
        return fun2(fun2(x,1),n-1) # if n!= 1, then take the value from previous iteration into the next iteration


def fun3(x,n):
    """
    the function calculates the value of f(x)=3.95*x-3.95*(x**2) through n times recursion
    
    parameters:
    x: a number in [0,1] 
    n: number of recursion 
    """
    if n==1:
        return 3.95*x-3.95*(x**2) #the end of recursion，also is the first time to cacalute the result
    else:
        return fun3(fun3(x,1),n-1) # if n!= 1, then take the value from previous iteration into the next iteration


#Test Case: x=0.5 and n=1, n = 10, n = 50, n = 100) (x = 0.9 and n = 100) 
print("When x = 0.5 , n = 1")
print("the answers return: ", fun1(0.5, 1), fun2(0.5, 1), fun3(0.5,1) )
print("When x = 0.5 , n = 2")
print("the answers return: ", fun1(0.5, 2), fun2(0.5, 2), fun3(0.5,2) )
print("When x = 0.5 , n = 10")
print("the answers return: ", fun1(0.5, 10), fun2(0.5, 10), fun3(0.5,10) )
print("When x = 0.5 , n = 50")
print("the answers return: ", fun1(0.5, 50), fun2(0.5, 50), fun3(0.5,50) )
print("When x = 0.5 , n = 100")
print("the answers return: ", fun1(0.5, 100), fun2(0.5, 100), fun3(0.5,100))
print("When x = 0.9 , n = 100")
print("the answers return: ", fun1(0.9, 100), fun2(0.9, 100), fun3(0.9,100))


"""
Comments on the result:
As we can see, wehn the iterations go up, the answers produced by the 3 functions are
different. This is because there is a boundary on storing decimal places. As the iterations go up.
the decimals are rounded off. So each iteration contains round off error. AS the iterations go up to 
100, the round off errors accumluate, which produce different values from the 3 functions 
"""
