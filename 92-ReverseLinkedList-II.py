# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        
        pre_head = ListNode(0, head)
        pre_cur = pre_head
        
        cnt = right - left
        
        while left > 1:
            left -= 1
            pre_cur = pre_cur.next
            #print(pre_cur.val)
            
        cur = pre_cur.next
        tail = cur
        new_head = None
        
        while cur and cnt >= 0:
                # print(cur.val)
                temp = cur.next
                cur.next = new_head
                new_head = cur
                cur = temp
                # print(cur.val)
                cnt -= 1
        
        tail.next = cur
        pre_cur.next = new_head
        
        return pre_head.next
        
