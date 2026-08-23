# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    # O(1) space complexity
    # Runtime: 41ms
    # Memory: 8.0 MB
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    # n is the number of nodes in the linked list
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        linked_list_length = 0
        curr = head

        while curr != None:
            linked_list_length += 1
            curr = curr.next
        
        node_to_remove = linked_list_length - n
        
        if node_to_remove == 0 and linked_list_length == 1:
            head = None
        elif node_to_remove == 0:
            temp = head.next
            head.next = None
            head = temp
        elif node_to_remove == linked_list_length - 1:
            count = 0
            curr = head

            while count < node_to_remove - 1:
                curr = curr.next
                count += 1
            
            curr.next = None
        else:
            count = 0
            curr = head

            while count < node_to_remove - 1:
                curr = curr.next
                count += 1
            
            temp = curr.next.next
            curr.next.next = None
            curr.next = temp

        return head
        