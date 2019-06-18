#Daily Coding Problem #11 [Medium]
#Implement an autocomplete system. That is, given a query string s
#and a set of all possible query strings, return all strings in the set that have s as a prefix.
#For example, given the query string de and the set of strings [dog, deer, deal], return [deer, deal].
def find_strings(lst, prefix):
    num = len(prefix)
    res = set()
    for i in lst:
        if num > len(i):
            continue
        else:
            if(i[0:num] == prefix):
                res.add(i)
    
    return list(res)

print(find_strings(["dog", "deer", "deal"],"de"))
