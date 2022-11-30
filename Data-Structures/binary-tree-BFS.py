""" Binary Tree - Breath First Search (BFS) """


class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def insert(self, data):
        if self.data is None:
            self.data = data
        else:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    # recursive call
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    # recursive call
                    self.right.insert(data)


root = Node(1)
root.insert(2)
root.insert(3)
root.insert(4)
