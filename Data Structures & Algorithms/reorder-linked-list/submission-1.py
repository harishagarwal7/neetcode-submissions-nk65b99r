# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        reverseHead=head
        headCopy=head
        head=head.next
        nodeCount=1
        while(head!=None):
            newNode=ListNode(head.val,reverseHead)
            head=head.next
            reverseHead=newNode
            nodeCount+=1
        head=headCopy
        lastReverseHead=ListNode()
        for i in range(nodeCount//2):
            nextHead=head.next
            nextReverseHead=reverseHead.next
            head.next=reverseHead
            reverseHead.next=nextHead
            head=nextHead
            lastReverseHead=reverseHead
            reverseHead=nextReverseHead
        if(nodeCount%2==0):
            lastReverseHead.next=None
        else:
            head.next=None
            lastReverseHead.next=head
        head=headCopy
            

        