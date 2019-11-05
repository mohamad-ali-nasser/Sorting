# TO-DO: Complete the selection_sort() function below 
def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index

        for j in range(i + 1, len(arr)):
            if arr[j] < arr[smallest_index]:
                smallest_index = j

        arr[smallest_index], arr[i] = arr[i], arr[smallest_index]

    return arr

# x = [1,2,3]
# print(x[0:3])
print(selection_sort([2,5,1,6,7,3,8,12]))

# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):

    for j in range(len(arr)):
        for i in range(len(arr)-1):
            if arr[i] < arr[i+1]:
                pass
            else:
                arr[i], arr[i+1] = arr[i+1], arr[i]
    return arr
print(bubble_sort([2,5,13,1,6,7,3,20,14,8,12]))

# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr