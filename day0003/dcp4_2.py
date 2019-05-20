#Daily Coding Problem #4 [Hard]
#Given an array of integers, find the first missing positive integer in linear time and constant space.
#In other words, find the lowest positive integer that does not exist in the array.
#The array can contain duplicates and negative numbers as well.
#For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.
#You can modify the input array in-place.

def find_missing(lst):
    i = 1
    while(True):
        try:
            ind = lst.index(i)
        except ValueError:
            return i
        else:
            i = i+1

print(find_missing([3, 4, -1, 1]))
print(find_missing([1, 2, 0]))
