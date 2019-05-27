#Daily Coding Problem #8 [Easy]
#A unival tree (which stands for "universal value") is a tree where all nodes under it have the same value.
#Given the root to a binary tree, count the number of unival subtrees.
#For example, the following tree has 5 unival subtrees:
#   0
#  / \
# 1   0
#    / \
#   1   0
#  / \
# 1   1
class Node:
    def __init__(self,val,left=None,right=None):
        self.val = val
        self.left = left
        self.right = right
        
def num_unival_trees(tree):
    count = 0
    if(tree == None):
        return 0
    if(tree.left.val == tree.right.val):
        count = count + 1
    return count + num_unival_trees(tree.left) + num_unival_trees(tree.right)
                          
print(num_unival_trees(Node(Node(0),Node(1),Node(Node(0),Node(Node(1),Node(1),Node(1)),Node(0)))))
