#Daily Coding Problem #9 [Hard]
#Given a list of integers, write a function that returns the largest sum of non-adjacent numbers.
#Numbers can be 0 or negative.
#For example, [2, 4, 6, 2, 5] should return 13, since we pick 2, 6, and 5.
#[5, 1, 1, 5] should return 10, since we pick 5 and 5.
#Follow-up: Can you do this in O(N) time and constant space?
def largest_non_adjacent(arr):
    if not arr:
        return 0

    return max(
            largest_non_adjacent(arr[1:]),
            arr[0] + largest_non_adjacent(arr[2:]))
                          
print(largest_non_adjacent([2,4,6,2,5]))
print(largest_non_adjacent([9,4,6,9,1,2]))
