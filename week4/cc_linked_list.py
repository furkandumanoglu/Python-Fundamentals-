class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def prepend(self, value):
        new_node = Node(value)  # Instantiate a new Node with the provided value
        if not self.head:  # If the list is empty, make the new node the head
            self.head = new_node
            print(f"Head Node created: {self.head.value}")
        else:  # Otherwise, insert the new node before the current head
            new_node.next = self.head
            self.head = new_node
            print(f"Prepended new Head Node with value: {self.head.value}")
            print(f"Node following Head is: {self.head.next.value}")

# Testing the LinkedList prepend method
llist = LinkedList()
llist.prepend("First Node")  # This should create the head node
llist.prepend("Inserted New First Node")  # This should prepend a new node and make it the new head