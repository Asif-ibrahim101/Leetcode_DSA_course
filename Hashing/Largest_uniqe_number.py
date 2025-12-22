#Given an integer array nums, return the largest integer that only occurs once. 
#If no integer occurs once, return -1.

# Example 1:
# Input: nums = [5,7,3,9,4,9,8,3,1]
# Output: 8
# Explanation: The maximum integer in the array is 9 but it is repeated. The number 8 occurs only once, so it is the answer.
# Example 2:

# Input: nums = [9,9,8,8]
# Output: -1
# Explanation: There is no number that occurs only once.

def LargestUniqueNumber(nums):
    frequency = {}
    
    # Count the frequency of each number in the array
    for num in nums:
        if num in frequency:
            frequency[num] += 1
        else:
            frequency[num] = 1
    
    largest_unique = -1
    
    # Find the largest number that occurs only once
    for num, count in frequency.items():
        if count == 1 and num > largest_unique:
            largest_unique = num
            
    return largest_unique