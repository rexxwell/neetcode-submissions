# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    # O(1) space complexity
    # Runtime: 155ms
    # Memory: 11.1 MB
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    # n is the number of nodes in the linked list.
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        linked_list_length = 0
        curr = head

        while curr != None:
            linked_list_length += 1
            curr = curr.next

        groups_of_k = linked_list_length // k
        new_head = None
        start_1 = head
        start_2 = None
        curr = head
        curr_next = curr.next if curr != None else None

        for i in range(groups_of_k):
            for j in range(k - 1):
                curr_temp = curr_next
                curr_next_temp = curr_next.next
                curr_next.next = curr
                curr = curr_temp
                curr_next = curr_next_temp

            if new_head == None:
                new_head = curr

            if i > 0 and start_1 != None:
                start_1.next = curr
                start_1 = start_2

            curr = curr_next
            curr_next = curr.next if curr != None else None
            start_2 = curr

        if linked_list_length % k == 0:
            start_1.next = None
        else:
            start_1.next = curr

        return new_head