# import random


# l = [1,2,3,4,5,6,7,8,9]
# left = []
# right = []

# cutoff = random.randrange(len(l))
# index = l.index(cutoff)
# for i in range(len(l)):
#     if i < index:
#         left.append(l[i])
#     else: 
#         right.append(l[i])

# print(cutoff)
# print(left)
# print(right)

class Node:
    def __init__(self,data):
        self.right=self.left=None
        self.data = data
class Solution:
    def insert(self,root,data):
        if root==None:
            return Node(data)
        else:
            if data<=root.data: # if the data is smaller or equal to the root
                cur=self.insert(root.left,data) # put it in the left branch
                root.left=cur
            else:
                cur=self.insert(root.right,data) # else put it in the right branch
                root.right=cur
        return root

    def getHeight(self,root):
        if not root:
            return 
        return 1 + max(self.getHeight(root.left), self.getHeight(root.right))

T=int(input())
myTree=Solution()
root=None
for i in range(T):
    data=int(input())
    root=myTree.insert(root,data)
height=myTree.getHeight(root)
print(height)      