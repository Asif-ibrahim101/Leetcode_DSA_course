def Check_Palendrome(s: str) -> bool:
    #using two pointers to solve the problem
    left = 0
    right = len(s) - 1

    while (left < right):
        if s[left] != s[right]:
            return False
        
        #increasing the pointers position
        left += 1
        right -= 1
    
    return True