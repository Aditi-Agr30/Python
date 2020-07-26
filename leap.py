# -*- coding: utf-8 -*-
"""
Created on Sun Jul 26 19:28:08 2020

@author: Aditi Agrawal
"""

year=int(input("Enter year you wish: "))
if((year%400==0) or (year%4==0) and (year%100!=0)):
    print(year," is leap year")
else:
    print(year," is not leap year")