arr1 = [1,2,3]
arr2 = [4,5,6,7]

#using two pointers to add arrays
def AddArrays(arr1, arr2):
    i = j = 0
    totalArr = []

    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            totalArr.append(arr1[i])
            i += 1
        else:
            totalArr.append(arr2[j])
            j += 1

    while i < len(arr1):
        totalArr.append(arr1[i])
        i += 1

    while j < len(arr2):
        totalArr.append(arr2[j])
        j += 1

    return totalArr

printArr = AddArrays(arr1, arr2)

print(printArr)
