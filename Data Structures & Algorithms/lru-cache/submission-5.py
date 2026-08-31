class DoublyLinkedList:

    def __init__(self, capacity: int, head: DoublyLinkedListNode = None, tail: DoublyLinkedListNode = None):
        self.capacity = capacity
        self.head = head
        self.tail = tail


class DoublyLinkedListNode:

    def __init__(self, key: int, value: int, next: DoublyLinkedListNode = None, prev: DoublyLinkedListNode = None):
        self.key = key
        self.value = value
        self.next = next
        self.prev = prev


class LRUCache:
    # Doubly Linked List and Hash Map
    # Runtime: 234ms
    # Memory: 15.4 MB
    # Time Complexity: O(1) per operation
    # Space Complexity: O(capacity)
    #   because the `hash_map` and `DoublyLinkedList` will hold a maximum of
    #   capacity number of nodes and entries.

    def __init__(self, capacity: int):
        self.doubly_linked_list = DoublyLinkedList(capacity)
        self.curr_capacity = 0
        self.hash_map = {}

    def get(self, key: int) -> int:
        if key in self.hash_map:
            # Move `self.hash_map[key]` into the most recently used.
            self._move_to_head(self.hash_map[key])

            return self.hash_map[key].value
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.hash_map:
            # Update the value.
            self.hash_map[key].value = value

            # Push the key to be the most recently used.

            # Move the node in `self.doubly_linked_list`
            # to be the new head.
            self._move_to_head(self.hash_map[key])
        else:
            # Check if the introduction of the new pair
            # causes the cache to exceed its capacity.
            if self.curr_capacity + 1 > self.doubly_linked_list.capacity:
                # Remove the least recently used key.
                old_tail_node = self.doubly_linked_list.tail
                
                # EDGE CASE 4: The cache only has 1 item (Head and Tail are the same)
                if self.doubly_linked_list.head == self.doubly_linked_list.tail:
                    self.doubly_linked_list.head = None
                    self.doubly_linked_list.tail = None
                # EDGE CASE 5: The cache has multiple items
                else:
                    self.doubly_linked_list.tail = old_tail_node.prev
                    self.doubly_linked_list.tail.next = None

                # Remove the key-value pair from `self.hash_map`.
                self.hash_map.pop(old_tail_node.key, None)

                # Decrement `curr_capacity`.
                self.curr_capacity -= 1
            
            # Add the new key-value pair to the cache.
            self.hash_map[key] = DoublyLinkedListNode(key, value)

            # Push the new key-value pair to be the most
            # recently used.
            if self.doubly_linked_list.head == None:
                self.doubly_linked_list.head = self.hash_map[key]
                self.doubly_linked_list.tail = self.hash_map[key]
            else:
                self.hash_map[key].next = self.doubly_linked_list.head
                self.doubly_linked_list.head.prev = self.hash_map[key]
                self.doubly_linked_list.head = self.hash_map[key]
            
            # Increment `curr_capacity`
            self.curr_capacity += 1

    # Done by AI.
    def _move_to_head(self, node: DoublyLinkedListNode):
        # EDGE CASE 1: The node is already the head. Do nothing.
        if node == self.doubly_linked_list.head:
            return

        # ----------------------------------------------------
        # STEP 1: Extract the node from its current position
        # ----------------------------------------------------
        
        # EDGE CASE 2: The node is at the tail
        if node == self.doubly_linked_list.tail:
            self.doubly_linked_list.tail = node.prev
            self.doubly_linked_list.tail.next = None
            
        # EDGE CASE 3: The node is in the middle
        else:
            node.prev.next = node.next
            node.next.prev = node.prev

        # ----------------------------------------------------
        # STEP 2: Place the extracted node at the head
        # ----------------------------------------------------
        node.next = self.doubly_linked_list.head
        node.prev = None
        
        # Link the old head back to this node
        self.doubly_linked_list.head.prev = node     
        self.doubly_linked_list.head = node