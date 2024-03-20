# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None
 
#     # Method to add a node at begin of LL
#     def insertAtBegin(self, data):
#         new_node = ListNode(data)
#         if self.head is None:
#             self.head = new_node
#             return
#         else:
#             new_node.next = self.head
#             self.head = new_node
 
#     # Method to add a node at any index
#     # Indexing starts from 0.
#     def insertAtIndex(self, data, index):
#         new_node = ListNode(data)
#         current_node = self.head
#         position = 0
#         if position == index:
#             self.insertAtBegin(data)
#         else:
#             while(current_node != None and position+1 != index):
#                 position = position+1
#                 current_node = current_node.next
 
#             if current_node != None:
#                 new_node.next = current_node.next
#                 current_node.next = new_node
#             else:
#                 print("Index not present")
 
#     # Method to add a node at the end of LL
 
#     def insertAtEnd(self, data):
#         new_node = ListNode(data)
#         if self.head is None:
#             self.head = new_node
#             return
 
#         current_node = self.head
#         while(current_node.next):
#             current_node = current_node.next
 
#         current_node.next = new_node
 
#     # Update node of a linked list
#         # at given position
#     def updateNode(self, val, index):
#         current_node = self.head
#         position = 0
#         if position == index:
#             current_node.data = val
#         else:
#             while(current_node != None and position != index):
#                 position = position+1
#                 current_node = current_node.next
 
#             if current_node != None:
#                 current_node.data = val
#             else:
#                 print("Index not present")
 
#     # Method to remove first node of linked list
 
#     def remove_first_node(self):
#         if(self.head == None):
#             return
 
#         self.head = self.head.next
 
#     # Method to remove last node of linked list
#     def remove_last_node(self):
 
#         if self.head is None:
#             return
 
#         current_node = self.head
#         while(current_node.next.next):
#             current_node = current_node.next
 
#         current_node.next = None
 
#     # Method to remove at given index
#     def remove_at_index(self, index):
#         if self.head == None:
#             return
 
#         current_node = self.head
#         position = 0
#         if position == index:
#             self.remove_first_node()
#         else:
#             while(current_node != None and position+1 != index):
#                 position = position+1
#                 current_node = current_node.next
 
#             if current_node != None:
#                 current_node.next = current_node.next.next
#             else:
#                 print("Index not present")
 
#     # Method to remove a node from linked list
#     def remove_node(self, data):
#         current_node = self.head
 
#         if current_node.data == data:
#             self.remove_first_node()
#             return
 
#         while(current_node != None and current_node.next.data != data):
#             current_node = current_node.next
 
#         if current_node == None:
#             return
#         else:
#             current_node.next = current_node.next.next
 
#     # Print the size of linked list
#     def sizeOfLL(self):
#         size = 0
#         if(self.head):
#             current_node = self.head
#             while(current_node):
#                 size = size+1
#                 current_node = current_node.next
#             return size
#         else:
#             return 0
    
    def printLL(self):
        current_node = self.head
        while(current_node):
            print(current_node.val)
            current_node = current_node.next

#     # print method for the linked list
#     def linked_list_to_list(head):
#         result = []
#         current = head
#         while current:
#             result.append(current.val)
#             current = current.next
#         return result

class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        # Encontrar o nó de índice a em list1
        node_before_a = list1
        for _ in range(a - 1):
            node_before_a = node_before_a.next
            print(node_before_a)

        # Encontrar o nó de índice b em list1
        node_b = node_before_a
        for _ in range(b - a + 2):
            node_b = node_b.next
        
        # Conectar o último nó de list2 ao nó de índice b em list1
        last_node_list2 = list2
        while last_node_list2.next:
            last_node_list2 = last_node_list2.next
        last_node_list2.next = node_b
        
        # Conectar o nó de índice a-1 em list1 ao primeiro nó de list2
        node_before_a.next = list2
        
        return list1

if __name__ == "__main__":
    access_solution = Solution()
    # list1 = [10,1,13,6,9,5]
    # a = 3
    # b = 4
    # list2 = [1000000,1000001,1000002]
    list1 = [0,1,2,3,4,5,6]
    a = 2
    b = 5
    list2 = [1000000,1000001,1000002,1000003,1000004]
    print(access_solution.mergeInBetween(list1, a, b, list2))
