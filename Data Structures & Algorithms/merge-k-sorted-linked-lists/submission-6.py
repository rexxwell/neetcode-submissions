import heapq


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    # Pointer Solution (With Min-Heap)
    # Runtime: 561ms
    # Memory: 14.4 MB
    # Time Complexity: O(nlogk)
    # Space Complexity: O(k)
    # n is the total number nodes across all linked list in `lists`.
    # k is the number of linked list in `lists`.
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        hash_map = {}
        min_heap = []
        head = None
        curr = head

        for i in range(len(lists)):
            if lists[i] != None:
                hash_map[i] = lists[i]
                heapq.heappush(min_heap, (lists[i].val, i))

        while len(hash_map) > 0:
            value, index = heapq.heappop(min_heap)
            min_list_node = hash_map[index]

            if head == None:
                head = min_list_node
                curr = head
            else:
                curr.next = min_list_node
                curr = curr.next

            min_list_node_next = min_list_node.next

            if min_list_node_next == None:
                hash_map.pop(index, None)
            else:
                hash_map[index] = min_list_node_next
                heapq.heappush(min_heap, (min_list_node_next.val, index))

        return head