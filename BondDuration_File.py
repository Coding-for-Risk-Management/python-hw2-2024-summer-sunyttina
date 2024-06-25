# -*- coding: utf-8 -*-
"""
Created on Tue Jun 25 15:07:11 2024

@author: surface
"""

#3
import numpy as np
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