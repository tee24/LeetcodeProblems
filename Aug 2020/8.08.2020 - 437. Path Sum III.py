class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        if not root:
            return 0
        count = 0
        nodes = []
        def traverse(root, nodes):
            if root:
                nodes = traverse(root.left, nodes)
                nodes.append(root)
                nodes = traverse(root.right, nodes)
            return nodes
                
        def dfs(root, path_sum, count):
            if path_sum == sum:
                count+=1
            if root:
                if root.left:
                    count = dfs(root.left, path_sum+root.left.val, count)
                if root.right:
                    count = dfs(root.right, path_sum+root.right.val, count)
            return count
        
        traverse(root, nodes)

        for node in nodes:
            count+=dfs(node, node.val, 0)
        return count

# Space, Time = O(n), O(n^2)