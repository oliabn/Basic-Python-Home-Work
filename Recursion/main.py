# binary tree

class Node:
    def __init__(self, data=None):
        self.left = None
        self.right = None
        self.data = data                        # поточний вузел

    def insert(self, new_node):                 # вставити new node
        if self.data:                               # Якщо вже існує data (потoчний вузел)
            if new_node < self.data:                    # Влiво
                if self.left is None:
                    self.left = Node(new_node)
                else:
                    self.left.insert(new_node)
            elif new_node > self.data:                  # Впрво
                if self.right is None:
                    self.right = Node(new_node)
                else:
                    self.right.insert(new_node)
        else:
            self.data = new_node                    # Вперше визначаємо потчний вузел - він же Root

    def print_tree(self):
        if self.left:
            self.left.print_tree()
        print(self.data)
        if self.right:
            self.right.print_tree()


my_tree = [1, 2, 10, 3, 5, 0]
root = Node()

for number in my_tree:
    root.insert(number)

root.print_tree()

