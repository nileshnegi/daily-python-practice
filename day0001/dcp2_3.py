#Daily Coding Problem #2 [Hard]
#Given an array of integers, return a new array such that each element at index i of the new array
#is the product of all the numbers in the original array except the one at i.
#Ex. if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24].
#If our input was [3, 2, 1], the expected output would be [2, 3, 6].
#Follow-up: what if you can't use division?
def product_array_nodiv_makers(lst):
    # Generate preffix products
    prefix_products = []
    for i in lst:
        if prefix_products:
            prefix_products.append(prefix_products[-1] * i)
        else:
            prefix_products.append(i)

    # Generate suffix products
    suffix_products = []
    for j in reversed(lst):
        if suffix_products:
            suffix_products.append(suffix_products[-1] * j)
        else:
            suffix_products.append(j)
    suffix_products = list(reversed(suffix_products))

    # Generate result
    new_lst = []
    for k in range(len(lst)):
        if k == 0:
            new_lst.append(suffix_products[k + 1])
        elif k == len(lst) - 1:
            new_lst.append(prefix_products[k - 1])
        else:
            new_lst.append(prefix_products[k - 1] * suffix_products[k + 1])
    
    #print(prefix_products)
    #print(suffix_products)
    return new_lst

print(product_array_nodiv_makers([1,2,3,4,5]))
print(product_array_nodiv_makers([3,2,1]))
