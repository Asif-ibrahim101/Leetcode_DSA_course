# Two pointers is an extremely common technique used to solve array and string problems. 
# It involves having two integer variables that both move along an iterable. 
# In this article, we are focusing on arrays and strings. 
# This means we will have two integers, 
# usually named something like i and j, or left 
# and right which each represent an index of the array or string.

#technique:
#create an left and right pointers from 0 to n - 1
#write an condition if the condition does'nt meets than return false
#increase the pointers from left++ and right--
#after the loop return the value True if its proven.

#sudo code
# def Pointers(n):
#     left = 0
#     right = len(n) - 1

#     #run an while loop
#     while left < right:
#         #do some procesing
#         #increase the left or the first pointer left++
#         #decrease the right or the 2nd pointer. right