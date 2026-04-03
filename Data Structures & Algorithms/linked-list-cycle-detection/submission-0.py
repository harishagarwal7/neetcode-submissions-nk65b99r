# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        headCopy=head
        while(head!=None and headCopy!=None and headCopy.next!=None):
            head=head.next
            headCopy=headCopy.next.next
            if(head==headCopy):
                return True
        return False
        