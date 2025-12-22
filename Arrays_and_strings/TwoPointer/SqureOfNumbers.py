#Given an integer array nums sorted in non-decreasing order, 
# return an array of the squares of each number sorted in non-decreasing order.

#Input: nums = [-4,-1,0,3,10]
# Output: [0,1,9,16,100]
import math

def GetSquire(nums):
    left = 0
    right = len(nums) - 1

    squired_Array = [0] * len(nums)
    pos = len(nums) - 1 #to fill from the end

    while(left <= right):
       left_Sq = nums[left] ** 2
       right_Sq = nums[right] ** 2

       if (left_Sq > right_Sq):
           squired_Array[pos] = left_Sq
           left += 1
       else:
           squired_Array[pos] = right_Sq
           right -= 1

    pos -= 1
    
    return squired_Array
