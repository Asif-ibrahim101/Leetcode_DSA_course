#template for solving prefix sum pattern problems using hashing and counting

#problem 1: given an integer arry nums and an integer K.
#find the number of subarrays whose sum is equal to k

from collections import defaultdict

class solution:
    def subarrays(self, nums: list[int], target: int) -> int :
        counts = defaultdict(int)
        counts[0] = 1
        ans = 0
        curr_sum = 0 #track the prefix sum

        #iterate over the array
        for num in nums:
            curr_sum += num

            #check if [curr_sum - target] is in the map or not
            ans += counts[curr_sum - target]
            counts[curr_sum] += 1
        
        return ans
    
#summary
#curr - track the prefix sum
#At any index i, the sum up to i is curr. 
# If there is an index j whose prefix is curr - k, 
# then the sum of the subarray with elements from 
# j + 1 to i is curr - (curr - k) = k.
#Because the array can have negative numbers, the same prefix can occur multiple times. 
#We use a hash map counts to track how many times a prefix has occurred.
#At every index i, the frequency of curr - k is 
# equal to the number of subarrays whose sum is equal to k that end at i. 
# Add it to the answer.

