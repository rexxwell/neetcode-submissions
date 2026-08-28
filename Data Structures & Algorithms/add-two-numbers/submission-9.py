# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    # O(1) space complexity
    # Runtime: 29ms
    # Memory: 8.0 MB
    # Time Complexity: O(max(n, m))
    # Space Complexity: O(1)
    # n is the number of nodes in l1.
    # m is the number of nodes in l2.
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        curr_l1 = l1
        curr_l2 = l2
        prev = curr_l1

        while curr_l1 != None or curr_l2 != None:
            curr_l1_val = curr_l1.val if curr_l1 != None else 0
            curr_l2_val = curr_l2.val if curr_l2 != None else 0
            sum_l1_l2_carry = curr_l1_val + curr_l2_val + carry
            remainder = sum_l1_l2_carry % 10
            
            if curr_l1 == None:
                prev.next = ListNode(remainder, None)
                curr_l1 = prev.next
            else:
                curr_l1.val = remainder

            carry = sum_l1_l2_carry // 10
            prev = curr_l1
            curr_l1 = curr_l1.next if curr_l1 != None else None
            curr_l2 = curr_l2.next if curr_l2 != None else None
        
        if carry != 0:
            prev.next = ListNode(carry, None)
        
        return l1