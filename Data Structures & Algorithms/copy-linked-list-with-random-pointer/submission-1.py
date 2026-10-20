"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        copyToMap = {None: None}
        cur = head
        while cur:
            copy = Node(cur.val)
            copyToMap[cur] = copy
            cur = cur.next

        cur = head
        while cur:
            copy = copyToMap[cur]
            copy.next = copyToMap[cur.next]
            copy.random = copyToMap[cur.random]
            cur = cur.next

        return copyToMap[head]
