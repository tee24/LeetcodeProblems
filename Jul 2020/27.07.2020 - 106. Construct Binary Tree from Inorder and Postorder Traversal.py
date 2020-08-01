class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        if inorder:
            root = TreeNode(postorder.pop())
            index = inorder.index(root.val)
            root.right = self.buildTree(inorder[index+1:], postorder)
            root.left = self.buildTree(inorder[:index], postorder)
            return root