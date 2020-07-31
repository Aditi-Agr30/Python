# -*- coding: utf-8 -*-
"""
Created on Thu Jul 30 11:28:00 2020

@author: Aditi Agrawal
"""

def insertion_sort(nums):
    # Start with 2nd item as we assume 1st to be sorted
    for i in range(1,len(nums)):
        item_to_insert = nums[i]
        # Keep a reference to previous item
        j = i-1
        # Move all itmes of sorted segment forward if they are larger than than the item to be inserted
        while j >= 0 and nums[j] > item_to_insert:
            nums[j+1] = nums[j]
            j -= 1
            #Insert the item
            nums[j+1] = item_to_insert


n = int(input("How many numbers you want to enter: "))
nums = []
for i in range(n):
    nums.append(int(input()))
insertion_sort(nums)
print(nums)