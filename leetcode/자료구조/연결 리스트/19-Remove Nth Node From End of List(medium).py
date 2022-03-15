# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        walker = runner = head
        
        for _ in range(n):
            runner = runner.next
            
        if not runner:
            return head.next
        
        while runner.next:
            walker = walker.next
            runner = runner.next
            
        walker.next = walker.next.next
        
        return head