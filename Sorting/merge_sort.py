def mergeSort(arr):

    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    leftHalf = arr[:mid]
    rightHalf = arr[mid:]

    sortedLeft = mergeSort(leftHalf)
    sortedRight = mergeSort(rightHalf)

    return _merge(sortedLeft, sortedRight)


def _merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):

        if left[i] > right[j]:
            result.append(left[i])
            i += 1

        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])

    return result


unsortedArr = [9,22,4,3,0,5,12,8,7,2,4,3,100]
sortedArr = mergeSort(unsortedArr)
print("Sorted array:", sortedArr)
