# Linear search O(n)
def name_in_phonebook(to_find, phonebook):
        for name in phonebook:   #O(size of phonebook) O(n)
            if name == to_find:
                return True
        
        return False
# Binary search, split the space in half each time, O(log n)
#
# Any time you're cutting the number of items to process down by
# half each step, you're likely in an O(log n) process
#
# log (base 2) is answering this question:
#     2 to the what power == x
#
# 65536 elements to process, 16 steps
# 32768 elements to process, 15 steps
# 16384
# 8192
# 4096
# 2048
# 1024
# 512
# 256
# 128
# 64
# 32
# 16
# 8
# 4
# 2
# 1
#
# You can double the number of items to process, and it only takes
# one more step! That's a lot of bang for the buck.
# Iterative binary search ("binary" because "binary" is 2, and we're
# dividing the search space by 2 each step)

def name_in_phonebook_binary_search(to_find, name):
    # sentinal edge case
    if len(to_find) == 0:
        return False
    # set first element to 0
    first = 0

    # set last to size - 1
    last = (len(to_find) - 1)

    # initialize found to False
    found = False

    # loop until either found or end of list
    while first <= last and not found:
        # find middle of the list using integer division
        middle = (first + last) // 2

        # if found update found variable
        if to_find[middle] == name:
            found = True
        else:
            if name < to_find[middle]:
                # search lower half of book
                last = middle - 1
            else:
                # search upper half of book
                first = middle + 1
    return found