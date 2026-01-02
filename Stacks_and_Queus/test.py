s = "helloo"

for i in range(len(s) - 1):        # go up to second-last index
    ch = s[i]
    nxt = s[i + 1]
    if ch == nxt:
        print("match at", i, ch, nxt)
