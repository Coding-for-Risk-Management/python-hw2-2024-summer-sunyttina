# -*- coding: utf-8 -*-
"""
Created on Tue Jun 25 15:07:11 2024

@author: surface
"""

import numpy as np

#2
def getBondPrice(y, face, couponRate, m, ppy=1):
    t=np.arange(0,ppy*m)
    cpn=couponRate*face/ppy
    df=(1/(1+y/ppy))
    dft=[df**(i+1) for i in t]
    bondPrice=cpn*sum(dft)+dft[-1]*face
    return(bondPrice)