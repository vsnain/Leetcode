# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        self.m = 0
        def dfs(root,l = 0, s = 100000):
            
            if root:
                if not root.left and not root.right:
                    s = min(s,root.val)
                    l = max(l,root.val)
                    self.m = max(self.m,abs(l-s))
                s = min(s,root.val)
                l = max(l,root.val)
                
                dfs(root.left,l,s)
                dfs(root.right,l,s)
        
        dfs(root)
        
        return self.m