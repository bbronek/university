class Node:

    def __init__(self, data):

        self.data = data
        self.left_child = None
        self.right_child = None

    def insert(self, data):

        if data < self.data:
            if not self.left_child:
                self.left_child = Node(data)
            else:
                self.left_child.insert(data)
        else:
            if not self.right_child:
                self.right_child = Node(data)
            else:
                self.right_child.insert(data)

    def remove(self, data, parent):

        if data < self.data:
            if self.left_child is not None:
                self.left_child.remove(data, self)

        elif data > self.data:
            if self.right_child is not None:
                self.right_child.remove(data, self)

        else:
            if self.left_child is not None and self.right_child is not None:
                self.data = self.right_child.get_min()
                self.right_child.remove(self.data, self)

            elif parent.left_child == self:

                if self.left_child is not None:
                    temporary = self.left_child

                else:
                    temporary = self.right_child

                parent.left_child = temporary

            elif parent.right_child == self:

                if self.left_child is not None:
                    temporary = self.left_child

                else:
                    temporary = self.right_child
                parent.right_child = temporary

    def get_min(self):

        if self.left_child is None:
            return self.data
        else:
            return self.left_child.get_min()

    def get_max(self):

        if self.right_child is None:
            return self.data
        else:
            return self.right_child.get_max()

    def traverse_in_order(self):

        if self.left_child is not None:
            self.left_child.traverse_in_order()

        print(self.data)

        if self.right_child is not None:
            self.right_child.traverse_in_order()


class BST:

    def __init__(self):

        self.root = None

    def insert(self, data):

        if not self.root:
            self.root = Node(data)
        else:
            self.root.insert(data)

    def remove(self, data):

        if self.root:

            if self.root.data == data:
                temporary = Node(None)
                temporary.left_child = self.root
                self.root.remove(data, temporary)
                self.root = temporary.left_child

            else:
                self.root.remove(data, None)

    def get_max(self):

        if self.root:
            return self.root.get_max()

    def get_min(self):

        if self.root:
            return self.root.get_min()

    def traverse_in_order(self):

        if self.root:
            self.root.traverse_in_order()


if __name__ == "__main__":
    bst = BST()
    for value in (12, 1, 9, -7):
        bst.insert(value)
    bst.remove(1)
    print(bst.get_min())
