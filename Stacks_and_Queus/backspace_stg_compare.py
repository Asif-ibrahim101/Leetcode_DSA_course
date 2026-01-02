# Example 3: 844. Backspace String Compare

# Given two strings s and t, 
# return true if they are equal when both are typed into empty text editors. 
# '#' means a backspace character.

# For example, given s = "ab#c" and t = "ad#c", 
# return true. Because of the backspace, the strings are both equal to "ac".

class solution:
    def backspace(self, s: str, t: str):
        def solve(str):
            stack = []

            for c in str:
                if c != "#":
                    stack.append(c)
                elif stack:
                    stack.pop()
            
            return "".join(stack)
        
        return solve(s) == solve(t)