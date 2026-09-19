class Node:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node


class LinkedList:
    def __init__(self):
        self.head = None
        self.counter = 0

    def traverse_list(self):
        node = self.head
        while node is not None:
            print(node.data)
            node = node.next_node

    def insert_start(self, data):
        self.head = Node(data, self.head)
        self.counter += 1

    def size(self):
        return self.counter

    def insert_end(self, data):
        if self.head is None:
            self.insert_start(data)
            return
        node = self.head
        while node.next_node is not None:
            node = node.next_node
        node.next_node = Node(data)
        self.counter += 1

    def remove(self, data):
        previous = None
        node = self.head
        while node is not None:
            if node.data == data:
                if previous is None:
                    self.head = node.next_node
                else:
                    previous.next_node = node.next_node
                self.counter -= 1
                return True
            previous, node = node, node.next_node
        return False


if __name__ == "__main__":
    linked_list = LinkedList()
    linked_list.insert_end(1)
    linked_list.insert_end(9)
    linked_list.insert_start(4)
    linked_list.traverse_list()
