# Given the head of a linked list, remove the nth node from the end of the list and return its head

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        fast = dummy
        slow = dummy

        for _ in range(n + 1): #so that slow stops one node before the target
            fast = fast.head
        

        while fast:
            slow = slow.next
            fast= fast.next
        
        slow.next = slow.next.next

        return dummy.next

