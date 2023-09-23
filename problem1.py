from os import *
from sys import *
from collections import *
from math import *



def sumOrProduct(n, q):


    if q == 1:
        summ = sum(n,start=0)
        print(summ)
    else :
        product = math.prod(n)
        print(product)
sumOrProduct([1,2,3,4,5],1)