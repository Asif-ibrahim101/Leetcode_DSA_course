#when ever we see an problem is asking about subarrays beign "valid" but also askes to find these 
#subarrays we should think about SLIDING WINDOW.

#sometimes they mayske about FIND THE NUMBER OF VALID SUBARRAYS.
#TYPE OF QUESTIONS THAT MAY COME.

#Find the longest subarray with a sum less than or equal to k (constraint metric = sum)
#Find the longest substring that has at most one "0" (constraint metric = number of zeroes)
#Find the number of subarrays that have a product less than k (constraint metric = product)

#IMPLEMENTATION OF SLIDINGWINDOW
#first we have to find the constraint matrix (which is the sum of the window)
#use the curr variable to keep track of the current sum
#when we are adding an element for the right we just increase the curr CURR += nums[right]
#when we remove an element form the left we just dicrease the curr CURR -= nums[left]
#by this way the time complexity becomes o(1)

#SUDO CODE OF THE IMPLEMENTATION
#functon fn(nums, k):
#   left = 0
#   curr = 0
#   answer = 0
#   for (int right = 0; right < nums.length; right++):
#           curr += nums[right]
#           while(curr > k):
#               curr -= nums[left]
#               left++
#           answer = max(answer, right - left + 1)
#   return answer

def find_length(nums: list[int], k: int):
    left = 0
    answer = 0
    curr = 0

    for right in range(len(nums)):
        curr += nums[right]

        while curr > k:
            curr -= nums[left]
            left += 1
        
        answer = max(answer, right - left + 1)
    return answer

