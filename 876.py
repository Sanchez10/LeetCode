# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def middleNode(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        head = ListNode()
        ahead = ListNode()

        ahead = head

        while ahead and ahead.next:
            ahead = ahead.next.next
            head = head.next
        
        return head
    