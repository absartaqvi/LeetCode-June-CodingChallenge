 Invert Binary Tree
'''
Example:

Input:

     4
   /   \
  2     7
 / \   / \
1   3 6   9
Output:

     4
   /   \
  7     2
 / \   / \
9   6 3   1
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        # Solution 1
        if root is None:
          return
        self.invertTree(root.left)
        self.invertTree(root.right)
        root.left, root.right = root.right, root.left
        return root

        # Solution 2
        '''queue = [root]  # [4]
        while queue:
          node = queue.pop(0)  # [], node = 4
          if node is None:
            continue
          queue.append(node.left)
          queue.append(node.right)
          node.left, node.right = node.right, node.left
        return root'''        
