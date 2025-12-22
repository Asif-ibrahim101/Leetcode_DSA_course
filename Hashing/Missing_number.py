#Given an array nums containing n distinct numbers in the range [0, n], 
# return the only number in the range that is missing from the array.

def missingNumber(nums):
    length = len(nums)
    seen = set(nums)

    for i in range(length + 1):
        if i not in seen:
            return i