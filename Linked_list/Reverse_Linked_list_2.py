# Given the head of a singly linked list and two integers left and right where left <= right, 
# reverse the nodes of the list from position left to position right, 
# and return the reversed list.

def Reverse_node(head, left, right):
    dummy = ListNode(0, head)
    prev = dummy

    for _ in range(left - 1):
        prev = prev.next
    

    curr = prev.next #which is the first value to be changed

    for _ in range(right - left): #going throw the range of the reverse window
        temp = curr.next
        curr.next = temp.next
        temp.next = prev.next
        prev.next = temp
    
    return dummy.next
