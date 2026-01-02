def template(nums):
    #use for problems like, “next greater”, “previous smaller”, “days until warmer”, “span”, “rectangle”.
    n - len(nums)
    ans = [-1] * n
    stack = [] #holds the indicess nums[stack] is decreasing

    for i in range(n):
        while stack and nums[i] > nums[stack[-1]]:
            j = stack.pop()
            ans[j] = nums[i]
        stack.append(i)

    return ans
       
