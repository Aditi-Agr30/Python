# -*- coding: utf-8 -*-
"""
Created on Thu Jul 30 11:21:51 2020

@author: Aditi Agrawal
"""

def selection_sort(nums):
    # i corresponds to how many values were sorted
    for i in range(len(nums)):
        # Assume that 1st item of unsorted segment is smallest
        lowest_value_index = i
        # Loop iterates over unsorted segment
        for j in range(i+1,len(nums)):
            if nums[j] < nums[lowest_value_index]:
                lowest_value_index = j
        # Swap values of lowest unsorted item with 1st unsorted item
        nums[i],nums[lowest_value_index] = nums[lowest_value_index],nums[i]
    
    
n = int(input("How many numbers you want to enter: "))
nums = []
for i in range(n):
    nums.append(int(input()))
selection_sort(nums)
print(nums)