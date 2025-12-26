def reverse(head):
    prev = None
    curr = head

    while curr:
        nextNode = curr.next
        curr.next = prev #reverse the dirrection of the pointer
        prev = curr #set the current node to the prev for the nextnode
        curr = nextNode #move on till the curr is null

    return prev