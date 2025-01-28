# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if list1 is None:
            return list2
        if list2 is None:
            return list1

        if list1.val <= list2.val:
            list1.next = self.mergeTwoLists(list1.next, list2)
            return list1
        else:
            list2.next = self.mergeTwoLists(list1, list2.next)
            return list2

# Helper function to create a linked list from a Python list
def create_linked_list(elements):
    head = None
    for element in reversed(elements):
        head = ListNode(val=element, next=head)
    return head

# Helper function to convert a linked list to a Python list
def linked_list_to_list(node):
    result = []
    while node:
        result.append(node.val)
        node = node.next
    return result

# Test cases
list1 = create_linked_list([1, 2, 4])
list2 = create_linked_list([1, 3, 4])

list3 = create_linked_list([])
list4 = create_linked_list([])

list5 = create_linked_list([])
list6 = create_linked_list([0])

solution = Solution()
merged_list = solution.mergeTwoLists(list1, list2)

# Convert the result back to a Python list and print it
result = linked_list_to_list(merged_list)
print("Merged list:", result)
