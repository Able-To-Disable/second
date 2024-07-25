from dataclasses import dataclass


@dataclass
class Node:
    def __init__(self, key):
        self.key = key
        self.next = None
        self.prev = None


class LinkedList:

    def __init__(self):
        self.head = None

    def insert_at_head(self, key):
        new_node = Node(key)
        new_node.next = self.head
        if self.head is not None:
            self.head.prev = new_node
        self.head = new_node

    def print_list(self):
        current = self.head
        while current is not None:
            print(current.key)
            current = current.next


linked_list = LinkedList()
linked_list.insert_at_head(3)
linked_list.insert_at_head(11)
linked_list.insert_at_head(7)
linked_list.print_list()
