#Given a string text, 
# you want to use the characters of text to form as many instances of the word "balloon" as possible.
# You can use each character in text at most once. 
# Return the maximum number of instances that can be formed.

# Input: text = "nlaebolko"
# Output: 1
# Example 2:

# Input: text = "loonbalxballpoon"
# Output: 2
# Example 3:

# Input: text = "leetcode"
# Output: 0

from collections import Counter, defaultdict

def maxNumberOfBalloons(text: str) -> int:
    map = defaultdict(int)

    for chat in text:
        map[chat] += 1
    
    b = map['b']
    a = map['a']
    l = map['l'] // 2
    o = map['o'] // 2
    n = map['n']

    return min(b, a, l, o, n)


    