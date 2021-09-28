"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
### ideas:
### 1) in order dfs traveerse/traveral {iteration && recursion}
### 2) Doubly Linked List     self.right = right
"""
class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        if not root:
            return None

        stack = [root]
        first, cur, last = None, root.left, None

        while cur or stack:
            if cur:
                stack.append(cur)
                cur = cur.left
                continue
            if stack:
                cur = stack.pop()
                if not first:
                    first = cur
                if last:
                    last.right = cur
                    cur.left = last
                last = cur
                cur = cur.right
        
        first.left = last
        last.right = first
        
        return first

