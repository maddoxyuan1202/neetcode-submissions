# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # 快慢指针 让 快指针 先走 n ， 然后两个一起走， fast指针none的时候慢指针就是倒数n， 切记此时快指针的状态
        fast, slow = head, head
        if not head or not head.next:
            return None

        for i in range(n):
            fast = fast.next
        
        if fast is None:
            return head.next

        while fast.next:
            slow = slow.next
            fast = fast.next
        
        slow.next = slow.next.next

        return head
        


