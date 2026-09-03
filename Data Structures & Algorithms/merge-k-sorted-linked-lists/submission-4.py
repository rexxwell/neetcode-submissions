# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    # Pointer solution where we have pointers at each index of lists.
    # Runtime: 2178ms (TLE)
    # Memory: 13.5 MB (TLE)
    # Time Complexity: O(nk)
    # Space Complaxity: O(k)
    # n is the total number of nodes in `lists` across all linked lists.
    # k is the number of linked lists in `lists`.
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        hash_map = {}
        linked_list_sorted_merged_head = None
        linked_list_sorted_merged_curr = linked_list_sorted_merged_head

        for i in range(len(lists)):
            if lists[i] != None:
                hash_map[i] = lists[i]

        while len(hash_map) > 0:
            min_index = -1
            min_list_node = ListNode(float('inf'), None)

            for index, list_node in hash_map.items():
                if list_node.val < min_list_node.val:
                    min_index = index
                    min_list_node = list_node
            
            min_list_node_next = min_list_node.next

            if min_list_node_next == None:
                hash_map.pop(min_index, None)
            else:
                hash_map[min_index] = min_list_node_next
            
            if linked_list_sorted_merged_head == None:
                linked_list_sorted_merged_head = min_list_node
                linked_list_sorted_merged_curr = linked_list_sorted_merged_head
            else:
                linked_list_sorted_merged_curr.next = min_list_node
                linked_list_sorted_merged_curr = linked_list_sorted_merged_curr.next

        return linked_list_sorted_merged_head