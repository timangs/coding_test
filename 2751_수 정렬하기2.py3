# -*- coding: utf-8 -*-
"""
Created on Thu Dec 30 14:08:18 2021

@author: jklee
"""

import sys

a =[int(sys.stdin.readline().strip()) for i in range(0,int(sys.stdin.readline().strip()))]
a = list(set(a))
a.sort()
for i in a:
    print(i)