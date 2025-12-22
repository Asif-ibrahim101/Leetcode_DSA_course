#Given a 2D array nums that contains n arrays of distinct integers, 
#return a sorted array containing all the numbers that appear in all n arrays.
#For example, given nums = [[3,1,2,4,5],[1,2,3,4],[3,4,5,6]], 
# return [3, 4]. 3 and 4 are the only numbers that are in all arrays.

from collections import defaultdict

class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        count = defaultdict(int)

        for arrs in nums:
            for x in arrs:
                count[x] += 1
            
        n = len(nums)
        ans = []

        for keys in count:
            if count[keys] == n:
                ans.append(keys)
            
        return sorted(ans)