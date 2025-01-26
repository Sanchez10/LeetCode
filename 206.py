# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def reverseList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        new_list = None

        while head:
            next_node = head.next
            head.next = new_list
            new_list = head
            head = next_node
        
        return new_list

if __name__ == "__main__":
    s = Solution()
    head = [1,2,3,4,5]
    head1 = [1,2]
    head2 = []
    new_list = s.reverseList(head)
