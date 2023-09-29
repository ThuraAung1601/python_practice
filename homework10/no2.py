'''
No. 2
Write a Python function to perform bubble sort of a list. 
Please study a bubble sort concept from the WWW.
'''
arr = [3, 2, 9, 7, 8, 1, 5, 4, 6]

def bubble_sort(arr):
    for i in range(len(arr)-1):
        for j in range(len(arr)-i-1):
                if arr[j] > arr[j+1]:
                    temp = arr[j]
                    arr[j] = arr[j+1]
                    arr[j+1] = temp  
    return arr

print(bubble_sort([3, 2, 9, 7, 8]))
# [2, 3, 7, 8, 9]

## bubble sort ascending/descending

# for i in range(len(arr)-1, 0, -1):
#     for j in range(i):
#         if arr[j] > arr[j+1]:
#             temp = arr[j]
#             arr[j] = arr[j+1]
#             arr[j+1] = temp
# print(arr)

# for i in range(len(arr)-1):
#     for j in range(len(arr)-i-1):
#         if arr[j] < arr[j+1]:
#             temp = arr[j]
#             arr[j] = arr[j+1]
#             arr[j+1] = temp
# print(arr)