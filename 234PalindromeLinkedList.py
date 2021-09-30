# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head.next: return True
        l_ = 1
        slow = fast = head
        while slow and fast and fast.next:
            l_ += 1
            slow = slow.next
            fast = fast.next.next
        
         
        new_head = None
        while slow:
            temp = slow.next
            slow.next = new_head
            new_head = slow
            slow = temp
        
        # while new_head:
        #     print(new_head.val)
        #     new_head = new_head.next
            
        
        
        while new_head:
            if new_head.val == head.val:
                new_head = new_head.next
                head = head.next234. Palindrome Linked List
            else:234. Palindrome Linked List
                return False
            
        return True
