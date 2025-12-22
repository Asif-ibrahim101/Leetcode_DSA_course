#Given a binary array (containing only 0s and 1s), 
#find the maximum length of a contiguous subarray with an equal number of 0s and 1s.

#intution: turn the problem into a sum problem than use the prefix_sum + hashmap template

# arr = [1, 1, 0, 1, 0] = 3,  [1, 1, -1, 1, -1] = 1

from collections import defaultdict

def solution(nums: list[int]):
    map = {}
    map[0] = -1 #storing the index not the freq because we need to find the length
    curr = 0
    max_len = 0

    for i, num in enumerate(nums):
        #turning the 0s into 1
        if num == 0:
            curr += -1
        else:
            curr += 1

        if curr in map:
            length = i - map[curr]
            max_len = max(max_len, length)
        else:
            map[curr] = i
    return max_len
    