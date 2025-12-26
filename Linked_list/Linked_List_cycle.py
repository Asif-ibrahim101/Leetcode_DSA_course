# Example 2: 141. Linked List Cycle
# Given the head of a linked list, determine if the linked list has a cycle.
# There is a cycle in a linked list if there is some node in the list 
# that can be reached again by continuously following the next pointer.

class solution: #it takes o(1) space and o(n) time
    def check_cycle(self, head) -> bool:
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:  #if the slow pointer meets the fast pointer at some point that means the list has a cycle
                return True
        
        return False


#the solution can also be done with hasing using a set() but it takes o(n) space comple but o(1) time
def check_cycle2(self, head) -> bool:
       seen = set()

       while head:
        if head in seen:
            return True
        seen.add(head)
        head = head.next

        return False
# This approach gives us a time complexity of 
# O(n)
# O(n) and a space complexity of 
# O(1)
# O(1), where n is the number of nodes in the linked list. 
# Note that this problem can also be solved using hashing, although it would require 
# O(n)
# O(n) space.