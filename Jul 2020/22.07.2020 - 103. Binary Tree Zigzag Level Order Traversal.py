# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from queue import Queue
from math import log2

class Solution:
    def height(self, root):
            if not root:
                return -1
            return 1 + max(self.height(root.left), self.height(root.right))
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return None
    
        h = self.height(root)
        ans = [[] for _ in range(h+1)]
        q = Queue()
        q.put([root,1])

        while q.qsize() > 0:
            node, pos = q.get()
            level = int(log2(pos))
            ans[level].append(node.val)

            if node.left:
                q.put([node.left, 2*pos])
            if node.right:
                q.put([node.right, 2*pos+1])

        for i, l in enumerate(ans):
            if i%2 == 1:
                ans[i] = l[::-1]

        return ans
        

def zigzagLevelOrder(root):
    if not root:
        return None

    positive_direction = 1
    q = Queue()
    q.put(root)
    ans = []

    while q.qsize() > 0:
        row = []
        for i in range(q.qsize()):
            node = q.get()
            row.append(node.val)
            
            if node.left:
                q.put(node.left)
            if node.right:
                q.put(node.right)
        ans.append(row[::positive_direction])
        positive_direction*=-1 #change direction

    return ans

# Space, Time: O(n), O(n) n = # of vertices (every vertex is visited once and stored in the list,ans.)