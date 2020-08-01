# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSameTree(self, p, q) -> bool:
    	def helper(root):
    		stack = []
    		stack.append([root, 1])
    		nodes = []
    		while len(stack)>0:
    			node, num = stack.pop()
    			nodes.append([node.val, num])
    			if node.left:
    				stack.append([node.left, 2*num])
    			if node.right:
    				stack.append([node.right, 2*num+1])
    		return nodes

    	tree_one = helper(p)
    	tree_two = helper(q)

    	return tree_one==tree_two

# Space, Time: O(n+m), O(n+m) n = number of p nodes, m = number of q nodes.

def isSameTree(self, p, q) -> bool:
	if not p and not q:
		return True
	if not p or not q:
		return False
	if p.val != q.val:
		return False

	return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)





    	
        