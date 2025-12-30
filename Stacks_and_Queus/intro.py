#stacks are fitst in last out. it has methods such as push, pop
#any dynamic array can implement a stack

#if we are using an dynamic array than the time complexity of a stack wll be
# o (1) constant time for push, pop and access but for search is O(n)

#we can also implememt a stack with a linked list with a tail pointer

#stack implementation
stack = []

#pushing elements
stack.append(1)
stack.append(2)
stack.append(3)

#poping elements
stack.pop()
stack.pop()

#check if the stack is empty or not
not stack

#check the element at the top
stack[-1]

#get size of a stack
len(stack)
