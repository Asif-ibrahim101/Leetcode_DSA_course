# You are given a string s and an integer k.
# Find the length of the longest substring that contains at most k distinct characters.
# For example, given s = "eceba" and k = 2, return 3. 
# The longest substring with at most 2 distinct characters is "ece".

from collections import defaultdict

def find_longest_sunstring(s, k):
    count = defaultdict(s)
    left = 0
    ans = 0

    for right in range(len(s)):
        count[s[right]] += 1

        while len(count) > k:
            count[s[left]] -= 1

            if count[s[left]] == 0:
                del count[s[left]]
            
            left += 1
        
        ans = max(left, right - left + 1)
    
    return ans