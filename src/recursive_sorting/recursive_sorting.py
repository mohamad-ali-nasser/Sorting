# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge( arrA, arrB ):
    elements = len( arrA ) + len( arrB )
    merged_arr = [0] * elements
    print(merged_arr)
    for i in range(len(arrA)):
        print(i)
        for j in range(len(merged_arr)):
            print(j)
            if arrA[i] > arrB[i]:
                merged_arr[j] = arrB[i]
            else:
                merged_arr[j] = arrA[i]
    
    return merged_arr

print(merge([1,2,3],[3,4,5]))

# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    # TO-DO

    return arr


# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr

def merge_sort_in_place(arr, l, r): 
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort( arr ):

    return arr

print(merge([1,2,3],[3,4,5]))