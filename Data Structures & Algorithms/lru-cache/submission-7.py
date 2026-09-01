class LRUCache:
    # Doubly Linked List and Hash Map
    # Dummy Head and Tail Optimization
    # `head.next` is the most recently used.
    # `tail.prev` is the least recently used.
    # Runtime: 240ms
    # Memory: 14.6 MB
    # Time Complexity: O(1)
    # Space Complexity: O(capacity)
    #   `self.hash_map` will have at most `capacity` number of entries.
    #   `self.doubly_linked_list` will have at most `capacity` number of nodes.

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.curr_capacity = 0
        head = DoublyLinkedListNode(-2, -2)
        tail = DoublyLinkedListNode(-2, -2)
        head.next = tail
        tail.prev = head
        self.doubly_linked_list = DoublyLinkedList(head, tail)
        self.hash_map = {}

    def get(self, key: int) -> int:
        if key in self.hash_map:
            # Move the `DoublyLinkedListNode` for the
            # key-value pair to the 'head' of the `DoublyLinkedList`
            # to be the most recently used.
            node = self.hash_map[key]
            self.doubly_linked_list._move_node_to_head(node)
            
            return node.value
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.hash_map:
            # Update the `value` of the `key` if the `key exists.
            node = self.hash_map[key]
            node.value = value
            self.doubly_linked_list._move_node_to_head(node)
        else:
            # Add the `key`-`value` pair to the cache.

            # Check if the introduction of the new pair causes the
            # cache to exceed its capacity, remove the least recently
            # used key.
            if self.curr_capacity == self.capacity:
                node_to_remove = self.doubly_linked_list.tail.prev
                self.doubly_linked_list._remove(node_to_remove)
                self.hash_map.pop(node_to_remove.key, None)
                self.curr_capacity -= 1

            node_to_add = DoublyLinkedListNode(key, value)
            self.doubly_linked_list._add_node_to_head(node_to_add)
            self.hash_map[key] = node_to_add
            self.curr_capacity += 1

class DoublyLinkedList:

    def __init__(self, head: DoublyLinkedListNode, tail: DoublyLinkedListNode):
        self.head = head
        self.tail = tail

    def _move_node_to_head(self, node: DoublyLinkedListNode) -> None:
        # If the `node` is already at the 'head' of the `DoublyLinkedList`,
        # then it is already the most recently used. Do nothing.
        if self.head.next == node:
            return
        else:
            # If the `node` is not at the 'head' of the `DoublyLinkedList`,
            # then we must move it to become the 'head' of the `DoublyLinkedList
            # to be the most recently used.
            self._remove(node)
            self._add_node_to_head(node)

    def _remove(self, node: DoublyLinkedListNode) -> None:
        node.prev.next = node.next
        node.next.prev = node.prev
        node.next = None
        node.prev = None

    def _add_node_to_head(self, node: DoublyLinkedListNode) -> None:
        node.next = self.head.next
        node.prev = self.head
        self.head.next = node
        node.next.prev = node


class DoublyLinkedListNode:

    def __init__(self, key: int, value: int, next: DoublyLinkedListNode = None, prev: DoublyLinkedListNode = None):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None