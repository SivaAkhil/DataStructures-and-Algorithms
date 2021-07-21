class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        currentNode = self

        while True:
        if value < currentNode.value:
            if currentNode.left is None:
                currentNode = currentNode.right
            else:
                currentNode = currentNode.left

    def contains(self, value):
        pass

    def remove(self, value, parentNode=None):
        pass
