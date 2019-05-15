#Daily Coding Problem #2 [Hard]
#Given an array of integers, return a new array such that each element at index i of the new array
#is the product of all the numbers in the original array except the one at i.
#Ex. if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24].
#If our input was [3, 2, 1], the expected output would be [2, 3, 6].
#Follow-up: what if you can't use division?
def product_array_nodiv(lst):
    res = 1
    new_lst = []
    for i in range(len(lst)):    
        for j in range(len(lst)):
            if j == i:
                continue
            else:
                res = res * lst[j]
        
        new_lst.append(int(res))
        res = 1
        
    return new_lst

print(product_array_nodiv([1,2,3,4,5]))
print(product_array_nodiv([3,2,1]))
