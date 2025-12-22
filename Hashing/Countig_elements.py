#Given an integer array arr, count how many elements x there are, 
# such that x + 1 is also in arr. 
# If there are duplicates in arr, count them separately

class Solution:
    def countElements(self, arr: list[int]) -> int:
        count = 0
        elements = set(arr)
        
        for x in arr:
            if x + 1 in elements:
                count += 1
                
        return count