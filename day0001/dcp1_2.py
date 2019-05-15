#Daily Coding Problem #1 [Easy]
#Given a list of numbers and a number k, return whether any two numbers from the list add up to k
#Ex. given [10,15,3,7] and k of 17, return true since 10+7 = 17
#Bonus: Can you do this in one pass?
##Using set() to create a set of numbers already seen in the list and check whether k-l[i] exists in this set
def check_sum_set(l,k):
    seen = set()
    for i in range(len(l)):
        if k-l[i] in seen:
            return True
        seen.add(l[i])
    return False

print(check_sum_set([10,15,3,7],10))
