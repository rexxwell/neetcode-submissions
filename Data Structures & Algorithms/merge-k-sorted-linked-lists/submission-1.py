# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    # Brute Force
    # Runtime: 298ms
    # Memory: 13.7 MB
    # Time Complexity: O(nmlog(nm))
    # Space Complexity: O(nm)
    # n is the number of linked list in lists.
    # m is the maximum number of nodes in lists[i]
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        linked_list_merged = []

        for list_node in lists:
            curr = list_node

            while curr != None:
                linked_list_merged.append(curr)
                curr = curr.next

        linked_list_sorted = sorted(linked_list_merged, key=lambda list_node: list_node.val)
        
        for i in range(len(linked_list_sorted) - 1):
            linked_list_sorted[i].next = linked_list_sorted[i + 1]
        
        if len(linked_list_sorted) > 0:
            linked_list_sorted[-1].next = None

            return linked_list_sorted[0]
        else:
            return None