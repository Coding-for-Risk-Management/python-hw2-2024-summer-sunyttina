# -*- coding: utf-8 -*-
"""
Created on Wed Jun 19 13:46:44 2024

@author: surface
"""
import numpy as np

#1
def WhoAmI():
    return('ys3713')

#2
def getBondPrice(y, face, couponRate, m, ppy=1):
    t=np.arange(0,ppy*m)
    cpn=couponRate*face
    df=(1/(1+y/ppy))
    dft=[df**(i+1) for i in t]
    bondPrice=cpn*sum(dft)+dft[-1]*face
    return(bondPrice)


# Test values

y = 0.03
face = 2000000
couponRate = 0.04
m=10
getBondPrice(y, face, couponRate, m, ppy=1)


#3
def getBondDuration(y, face, couponRate, m, ppy=1):
    t=np.arange(0,ppy*m)
    cpn=couponRate*face
    df=(1/(1+y/ppy))
    dft=[df**(i+1) for i in t]
    dftt=[df**(i+1) *(i+1) for i in t]
    bondPrice=cpn*sum(dft)+dft[-1]*face
    bondPricet=cpn*sum(dftt)+dftt[-1]*face
    BondDuration=bondPricet/bondPrice   
    return(BondDuration)
    

# Test values
y = 0.03
face = 2000000
couponRate = 0.04
m = 10
ppy = 1
getBondDuration(y, face, couponRate, m, ppy=1)



#4
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