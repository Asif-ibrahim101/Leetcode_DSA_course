#Given an array of integers nums and an integer target, 
#return indices of two numbers such that they add up to target. 
#You cannot use the same index twice.

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dis = {}

        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in dis:
                return [dis[complement], i]
            dis[nums[i]] = i