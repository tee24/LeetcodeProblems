# Definition for a binary tree node.
from queue import Queue
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:

    def height(self,root):
        if not root:
            return -1
        return 1+max(self.height(root.left), self.height(root.right))

    def widthOfBinaryTree(self, root: TreeNode) -> int:
        if not root:
            return None

        height = self.height(root)

        s = Queue()
        s.put([root, 1, 1])
        tree = [[] for _ in range(height+1)]
        first = True

        while not s.empty():
            node = s.get()
            if node[1] > height+1:
                break

            tree[node[1]-1].append(node[2])
            
            if node[0].left:
                s.put([node[0].left, node[1]+1, 2*node[2]])

            if node[0].right:
                s.put([node[0].right, node[1]+1, 2*node[2]+1])
            

        max_width = 0
        
        for i in tree:
            max_width = max(max_width, i[-1]-i[0]+1)

        return max_width

