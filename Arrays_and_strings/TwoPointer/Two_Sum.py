#Example 2: Given a sorted array of unique integers and a target integer, 
# return true if there exists a pair of numbers that sum to target, false otherwise. 
# This problem is similar to Two Sum. (In Two Sum, the input is not sorted).

nums = [1, 2, 4, 6, 8, 9, 14, 15]
target = 13

def Two_Sum(arr, target) :
    left = 0
    right = len(arr) - 1

    while (left < right):
        total = arr[left] + arr[right]

        if total == target:
            return True
        elif total > target:
            right -= 1
        else:
            left += 1
    
    return False



solution_check = Two_Sum(nums, target)
print(solution_check)