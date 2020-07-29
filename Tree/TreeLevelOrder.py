### BFS traversal

class BinaryTree(object):
    def __init__(self, value):
        self.value = value
        self.leftChild = None
        self.rightChild = None

    def insertLeft(self, newData):
        if self.leftChild is None:
            self.leftChild = BinaryTree(newData)
        else:
            t = BinaryTree(newData)
            t.leftChild = self.leftChild
            self.leftChild = t

    def insertRight(self, newData):
        if self.rightChild is None:
            self.rightChild = BinaryTree(newData)
        else:
            t = BinaryTree(newData)
            t.rightChild = self.rightChild
            self.rightChild = t

    def BFS(self):

        items = [self]

        while items:
            currentNode = items.pop(0)
            print(currentNode.value)

            if currentNode.leftChild:
                items.append(currentNode.leftChild)

            if currentNode.rightChild:
                items.append(currentNode.rightChild)

root_node = BinaryTree("34")

root_node.insertLeft("23")
root_node.insertRight("54")

node_b = root_node.leftChild
node_b.insertLeft("12")
node_b.insertRight("30")

node_c = root_node.rightChild
node_c.insertLeft("45")
node_c.insertRight("60")

root_node.BFS()