class ListNode:
    def __init__(self, val, next = None):
        self.val = val
        self.next = next
    

    def __str__ (self):
        return str(self.val)
    
Head = ListNode(1)
A = ListNode(2)
B = ListNode(5)
C = ListNode(10)

Head.next = A
A.next = B
B.next = C

# print(Head)

#traversal
def Traversal(head):
    curr = head

    while curr:  #it stops when the class val is null or at the tail which is c in this case
        print(curr)
        curr = curr.next

# Traversal(Head)


#display the linked list
def Display(head): #time complexity will be o(n)
    curr = head
    arr = []

    while curr:
        arr.append(str(curr.val))
        curr = curr.next
    
    print(' -> '.join(arr))

# Display(Head)

#search for a value time complexity 0(n)
def Search(head, val):
    curr = head

    while curr:
        if val == curr.val: #if we found it return true
            return True
        
        #we increment the next pointer
        curr = curr.next
    

    #if the loop ends and we havent found it that means return flase
    return False

print(Search(Head, 7))
