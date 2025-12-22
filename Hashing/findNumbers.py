#Given an integer array nums, 
# find all the numbers x in nums that satisfy the 
# following: 
#x + 1 is not in nums, and x - 1 is not in nums.

def find_numbers(nums):

    nums_set = set(nums)
    ans = []

    for num in nums_set:
        if (num + 1 not in nums_set) and (num - 1 not in nums_set):
            ans.append(num)
    return ans
        
        
