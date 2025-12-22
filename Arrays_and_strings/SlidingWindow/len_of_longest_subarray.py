def FindAnswer(arr, k):
    curr = 0
    left = 0
    answer = 0

    for right in range(len(arr)):
        curr += arr[right]
    
        while (curr > k):
            curr -= arr[left]
            left += 1
        answer = max(answer, right - left + 1)
    
    return answer
