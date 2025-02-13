# merge_sort.py - Tri fusion

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result
#merge([2,4,3,5,7,2,0,4], [3,2,5,1,7,5,98,44])
print(merge_sort(merge([2,4,3,5,7,2,0,4], [3,2,5,1,7,5,98,44])))
