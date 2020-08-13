from typing import List
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
    	if not root:
    		return None
 
    	stack = []
    	nodes = []
    	stack.append([root, 0, 0])
    	x_min = 0
    	x_max = 0

    	while stack:
    		temp = stack.pop()
    		node = temp[0]
    		nodes.append(temp)
    		x_min = min(x_min, temp[1])
    		x_max = max(x_max, temp[1])

    		if node.left:
    			stack.append([node.left, temp[1]-1, temp[2]-1])
    		if node.right:
    			stack.append([node.right, temp[1]+1, temp[2]-1])

    	x_length = x_max-x_min+1

    	nodes = sorted(nodes, key=lambda x: (-x[2], x[0].val))
    	ans = [[] for _ in range(x_length)]


    	for item in nodes:
    		item[1]+=abs(x_min)
    		ans[item[1]].append(item[0].val)

    	return ans


        