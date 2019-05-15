#Daily Coding Problem #1 [Easy]
#Given a list of numbers and a number k, return whether any two numbers from the list add up to k
#Ex. given [10,15,3,7] and k of 17, return true since 10+7 = 17
#Bonus: Can you do this in one pass?
##Using sort() to sort this list and use binary search to look for k-l[i] in this sorted list
from bisect import bisect_left
def binary_search(l,target):
    low = 0
    high = len(l)
    index = bisect_left(l,target,low,high)
    
    if ((low <= index < high) and l[index] == target):
        return index
    return -1

def check_sum_sortsearch(l,k):
    l.sort()
    for i in range(len(l)):
        target = k-l[i]
        j = binary_search(l,k-l[i])
        
        if j == -1:
            continue
        elif j != i:
            return True
        elif j+1 < len(l) and l[j+1] == target:
            return True
        elif j-1 >= 0 and l[j+1] == target:
            return True
        
    return False

print(check_sum_sortsearch([10,15,3,7],18))
