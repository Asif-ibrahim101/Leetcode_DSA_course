#Given an array of positive integers nums and an integer k. 
# Find the number of subarrays with exactly k odd numbers in them.For example, 
# given 
# nums = [1, 1, 2, 1, 1], k = 3, 
# the answer is 2. 
# The subarrays with 3 odd numbers in them are [1, 1, 2, 1, 1] and [1, 1, 2, 1, 1].


from collections import defaultdict

def solution(nums: list[int], K: int):
    counts = defaultdict(int)
    counter = 0
    counts[0] = 1
    ans = 0

    for num in nums:
        counter += num % 2
        ans += counts[counter - K]

        counts[counter] += 1
    
    return ans