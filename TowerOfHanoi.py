# -*- coding: utf-8 -*-
"""
Created on Sun Jul 26 15:56:10 2020

@author: Aditi Agrawal
"""

def TowerOfHanoi(disk,source,destination,auxiliary):
    if disk==1:
        print("Move disk 1 from ",source," to ",destination)
        return
    TowerOfHanoi(disk-1,source,auxiliary,destination)
    print("Move disk ",disk," from ",source," to ",destination)
    TowerOfHanoi(disk-1,auxiliary,destination,source)
    
disk=int(input("Enter the number of disks: "))
TowerOfHanoi(disk,'A','C','B')