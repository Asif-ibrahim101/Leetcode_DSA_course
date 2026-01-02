def Template(arr_to_string):
    stack = []

    for ch in arr_to_string:
        if stack and matches(stack[-1], ch):
            stack.pop()
        else:
            stack.append(ch)
        
    return stack #or "".join(stack)

#ways to think
#1. the stack holds the stafs that are not resolved yer
#2. if it mathches or rsolves pop it
#3. or else keep pushing in the stack
#4. return the stack or join the stack or string