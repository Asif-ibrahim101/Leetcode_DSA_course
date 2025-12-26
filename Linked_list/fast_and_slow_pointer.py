#its a two pointer implementation
# the "fast" pointer moves two nodes per iteration, whereas the "slow" pointer moves one node per iteration

#problem 1
# Given the head of a linked list with an odd number of nodes head, return the value of the node in the middle.
# For example, given a linked list that represents 1 -> 2 -> 3 -> 4 -> 5, return 3.


#using the slow and fast poiter which they star from the head and when the fast pointer reaches at the end or the tail the 
#slow pointer comes to the middle of the list so we just return the list
def find_middle(head):
    slow =head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    

    return slow.val

# The most elegant solution comes from using the fast and slow pointer technique. 
# If we have one pointer moving twice as fast as the other, 
# then by the time it reaches the end, 
# the slow pointer will be halfway through since it is moving at half the speed.

def get_middle(head):
    slow = head
    fast = head

    while fast and fast.next:
       slow = slow.next
       fast = fast.next.next
    
    return slow.val
    