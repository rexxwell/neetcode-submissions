# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    # Optimized O(1) space complexity
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        val_l1_l2 = l1.val + l2.val
        head_l1_l2 = ListNode(val_l1_l2 % 10, ListNode(val_l1_l2 // 10, None))

        if val_l1_l2 // 10 == 0:
            last_l1_l2 = head_l1_l2
        else:
            last_l1_l2 = head_l1_l2.next

        curr_l1 = l1.next
        curr_l2 = l2.next
        curr_l1_l2 = head_l1_l2.next

        while curr_l1 != None and curr_l2 != None:
            val_sum = curr_l1_l2.val + curr_l1.val + curr_l2.val
            curr_l1_l2.val = val_sum % 10
            curr_l1_l2.next = ListNode(val_sum // 10, None)
            curr_l1 = curr_l1.next
            curr_l2 = curr_l2.next
            
            if val_sum // 10 == 0:
                last_l1_l2 = curr_l1_l2
            else:
                last_l1_l2 = curr_l1_l2.next

            curr_l1_l2 = curr_l1_l2.next
        
        while curr_l1 != None:
            val_sum = curr_l1_l2.val + curr_l1.val
            curr_l1_l2.val = val_sum % 10
            curr_l1_l2.next = ListNode(val_sum // 10, None)
            curr_l1 = curr_l1.next
            
            if val_sum // 10 == 0:
                last_l1_l2 = curr_l1_l2
            else:
                last_l1_l2 = curr_l1_l2.next

            curr_l1_l2 = curr_l1_l2.next
        
        while curr_l2 != None:
            val_sum = curr_l1_l2.val + curr_l2.val
            curr_l1_l2.val = val_sum % 10
            curr_l1_l2.next = ListNode(val_sum // 10, None)
            curr_l2 = curr_l2.next
            
            if val_sum // 10 == 0:
                last_l1_l2 = curr_l1_l2
            else:
                last_l1_l2 = curr_l1_l2.next

            curr_l1_l2 = curr_l1_l2.next

        last_l1_l2.next = None

        return head_l1_l2