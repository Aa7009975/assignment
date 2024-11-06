# -*- coding: utf-8 -*-
"""
Created on Wed Nov  6 08:36:42 2024

@author: sa939
"""

def rectangle(m,n):
    for i in range(0,m):
        for j in range(0,n):
            print("*", end=" ")
        print("\n")

rectangle(2,4)