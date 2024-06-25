# -*- coding: utf-8 -*-
"""
Created on Tue Jun 25 15:07:11 2024

@author: surface
"""

#4
import numpy as np
def FizzBuzz(start, finish):
    fbRange=np.arange(start,finish+1)
    mod3=np.mod(fbRange,3)
    mod5=np.mod(fbRange,5)
    mod3Zeros=np.where(mod3==0)
    mod5Zeros=np.where(mod5==0)

    fizzbuzz=fbRange.astype(object)
    fizzbuzz[mod3Zeros] ="fizz"
    fizzbuzz[mod5Zeros]="buzz"
    fizzbuzz [np.intersect1d(mod3Zeros, mod5Zeros)]="fizzbuzz"
    return(fizzbuzz)

#test value
FizzBuzz(76,90)