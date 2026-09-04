# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    # Brute Force
    # Runtime: 167ms
    # Memory: 10.9 MB
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    # n is the number of nodes in the linked list.
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        linked_list = []
        curr = head

        while curr != None:
            linked_list.append(curr)
            curr = curr.next
        
        linked_list_reversed = []

        for i in range(len(linked_list) // k):
            for j in range(i * k + k - 1, i * k - 1, -1):
                linked_list_reversed.append(linked_list[j])

        if len(linked_list) % k != 0:
            for i in range(k * (len(linked_list) // k), len(linked_list)):
                linked_list_reversed.append(linked_list[i])
        
        for i in range(len(linked_list_reversed) - 1):
            linked_list_reversed[i].next = linked_list_reversed[i + 1]

        linked_list_reversed[-1].next = None

        return linked_list_reversed[0] if linked_list_reversed[0] != None else None