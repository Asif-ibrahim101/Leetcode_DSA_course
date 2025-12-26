class double:
    def __init__(self, val, next = None, prev = None):
        self.val = val
        self.next = next
        self.prev = prev
    

    def __str__(self):
        return str(self.val)

#display the linked list in a nice way
def display(head):
    curr = head
    elements = []

    while curr:
        elements.append(str(curr.val))
        curr = curr.next

    print(' <-> '.join(elements))

#adding a node [inserting at the begaining]
def inseart_at_the_begaining(head, tail, val):
    new_node = double(val, next= head)
    head.prev = new_node

    return new_node, tail

#adding a node at the end of a linked list
def inseart_at_the_end(head, tail, val):
    new_node = double(val, prev = tail)
    tail.prev = new_node

    return new_node, head

#removing from start o(1)
def remove_node_from_start():
    if head.next == tail:
        return
    
    node_to_remove = head.next
    node_to_remove.next.prev = head
    head.next = node_to_remove.next

#removing form end o(1)
def remove_from_end():
    if head.next == tail:  #if there is only one ele
        return
    
    node_to_remove = tail.prev
    node_to_remove.prev.next = tail
    tail.prev = node_to_remove.prev


#getting sum of all th elements for a linstdlistr
def get_sum(head):
    ans = 0

    #using a dummy pointer to point to the head
    dummy = head

    while dummy:
        ans += dummy.val
        dummy = dummy.next
    
    return ans


head = ListNode(None)
tail = ListNode(None)
head.next = tail
tail.prev = head
