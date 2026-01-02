# Input:s ="leEeetcode"
# Output: "leetcode"
# Explanation: In the first step, either you choose i = 1 or i = 2, both will result "leEeetcode" to be reduced to "leetcode".


def solution(word):
    stack = []

    for ch in word:
        if stack and stack[-1] != ch and stack[-1].lower() == ch.lower():
            stack.pop()
        else:
            stack.append(ch)
    
    return "".join(stack)


word = "leEeetcode"
print(solution(word))
