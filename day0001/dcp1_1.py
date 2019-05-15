#Daily Coding Problem #1 [Easy]
#Given a list of numbers and a number k, return whether any two numbers from the list add up to k
#Ex. given [10,15,3,7] and k of 17, return true since 10+7 = 17
#Bonus: Can you do this in one pass?

def check_sum(l,k):
    for i in range(len(l)):
        for j in range(i,len(l)):
            if(l[i]+l[j] == k):
                return True
    return False

print(check_sum([10,15,3,7],13))
