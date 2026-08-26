# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    # Brute Force
    # Runtime: 28ms
    # Memory: 8.0 MB
    # Time Complexity: O(nm)
    # Space Complexity: O(nm)
    # n is the number of nodes in linked_list_l1
    # m is the number of nodes in linked_list_l2
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        linked_list_l1 = []
        curr_l1 = l1

        while curr_l1 != None:
            linked_list_l1.append(curr_l1)
            curr_l1 = curr_l1.next
        
        linked_list_l2 = []
        curr_l2 = l2

        while curr_l2 != None:
            linked_list_l2.append(curr_l2)
            curr_l2 = curr_l2.next
        
        number_l1 = ""

        for i in range(len(linked_list_l1) - 1, -1, -1):
            number_l1 += str(linked_list_l1[i].val)
        
        number_l2 = ""

        for i in range(len(linked_list_l2) - 1, -1, -1):
            number_l2 += str(linked_list_l2[i].val)
        
        sum_l1_l2 = str(int(number_l1) + int(number_l2))
        linked_list_sum = []

        for i in range(len(sum_l1_l2) - 1, -1, -1):
            linked_list_sum.append(ListNode(int(sum_l1_l2[i])))
        
        for i in range(len(linked_list_sum) - 1):
            linked_list_sum[i].next = linked_list_sum[i + 1]

        return linked_list_sum[0]
        
