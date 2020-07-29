class BinarySearchTree(object):
    def __init__(self, value):
        self.value = value
        self.leftChild = None
        self.rightChild = None

    def insertNode(self, newData):

        if newData <= self.value and self.leftChild:
            self.leftChild.insertNode(newData)
        elif newData <= self.value:
            self.leftChild = BinarySearchTree(newData)

        if newData > self.value and self.rightChild:
            self.rightChild.insertNode(newData)
        elif newData > self.value:
            self.rightChild = BinarySearchTree(newData)

    def trimTree(self, minVal, maxVal):
        if not self:
            return

        if self.leftChild:
            self.leftChild.trimTree(minVal, maxVal)

        if self.rightChild:
            self.rightChild.trimTree(minVal, maxVal)

        if minVal <= self.value <= maxVal:
            return self

        if self.value < minVal:
            return self.rightChild

        if self.value > maxVal:
            return self.leftChild

def inOrder(root):

    if root.leftChild:
        inOrder(root.leftChild)

    print(root.value)

    if root.rightChild:
        inOrder(root.rightChild)


bst = BinarySearchTree(25)

bst.insertNode(10)
bst.insertNode(12)
bst.insertNode(20)
bst.insertNode(17)
bst.insertNode(15)
bst.insertNode(29)
bst.insertNode(30)
bst.trimTree(15, 30)
inOrder(bst)