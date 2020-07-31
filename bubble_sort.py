# -*- coding: utf-8 -*-
"""
Created on Thu Jul 30 11:10:40 2020

@author: Aditi Agrawal
"""

def bubble_sort(nums):
    # Set swapped to True so the loop looks run atleast once
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(nums)-1):
            if nums[i]>nums[i+1]:
                # Swapping the elements if condition is satisfied
                nums[i],nums[i+1] = nums[i+1],nums[i]
                swapped = True
    
n = int(input("How many numbers you want to enter: "))
nums = []
for i in range(n):
    nums.append(int(input()))
bubble_sort(nums)
print(nums)