#Given a string s, determine if all characters have the same frequency.
#For example, given s = "abacbc", return true, because all characters appear twice. 
#Given s = "aaabb", return false.
#"a" appears 3 times, "b" appears 2 times. 3 != 2.

from collections import defaultdict

def check(s):
    #if an key does not exits yet run the function int() to create a starting value. returns 0
    seen = defaultdict(int)

    for ch in s:

        #incrementing the dict
        seen[ch] += 1
    
    freq = seen.values()

    #check if the len of the set is 1. if its 1 means that the freq is repeating because set removes all the duplicates 
    checking_freq = len(set(freq)) == 1

    return checking_freq
