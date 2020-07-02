from queue import Queue

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrderBottom(self, root):
        if not root: # If there is no root then there is nothing to traverse.
            return None
        temp = []
        q = Queue()
        q.put([root,0])

        while not q.empty(): # BFS using Queue, whilst tracking level.
            node_level = q.get()
            node = node_level[0]
            temp.append([node_level[0].val, node_level[1]])
            if node.left:
                q.put([node.left, node_level[1]+1])
            if node.right:
                q.put([node.right, node_level[1]+1])
        
        top = -1

        for item in temp: # How many levels in the tree.
            top = max(top, item[1])

        ans = [[] for _ in range(top+1)]

        for item in temp: # From temp create the final answer
            ans[item[1]].append(item[0])

        return ans[::-1]

# Space & Time: O(n)