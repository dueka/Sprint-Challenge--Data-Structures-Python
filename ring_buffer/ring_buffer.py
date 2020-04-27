from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):
        if self.storage.length < self.capacity:
            self.storage.add_to_tail(item)
            self.current = self.storage.head
        else:
            old_node = self.storage.head
            self.storage.remove_from_head()
            self.storage.add_to_tail(item)
            if old_node == self.current:
                self.current = self.storage.tail

    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []

        # TODO: Your code here
        list_buffer_contents.append(self.current.value)
        if self.current == self.storage.tail:
            node = self.storage.head
        else:
            node = self.current.next

        if node is not self.current:
            list_buffer_contents.append(node)
            node = node.next
        return list_buffer_contents

# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass
