# Gavin Howard
# 3/2/2020
# Advanced Programming


class Node:
    def __init__(self, data=None, prev=None, next=None):
        self.data = data
        self.prev = prev
        self.next = next

    def __repr__(self):
        return repr(self.data)


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def __repr__(self):
        nodes = []
        curr = self.head
        while curr:
            nodes.append(repr(curr))
            curr = curr.next
        return '[' + ', '.join(nodes) + ']'

    def add_head(self, data):
        new_head = Node(data=data, next=self.head)
        if self.head:
            self.head.prev = new_head
        self.head = new_head

    def add_end(self, data):
        if not self.head:
            self.head = Node(data=data)
            return
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = Node(data=data, prev=curr)

    def remove_end(self):
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.prev.next = None
        return curr.data

    def remove_head(self):
        value = self.head.data
        self.head = self.head.next
        self.head.prev = None
        return value
