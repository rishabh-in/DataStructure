class BinarySearchTree(object):
    def __init__(self, value):
        self.value = value
        self.leftChild = None
        self.rightChild = None

    ###### 3 main operation - Insertion, Searching, Deletion

    ## 1 - Insertion

    def insertNode(self, newData):

        if newData <= self.value and self.leftChild:
            self.leftChild.insertNode(newData)
        elif newData <= self.value:
            self.leftChild = BinarySearchTree(newData)

        if newData > self.value and self.rightChild:
            self.rightChild.insertNode(newData)
        elif newData > self.value:
            self.rightChild = BinarySearchTree(newData)

    ## 2 - Searching

    def searchNode(self, value):

        if value < self.value and self.leftChild:
            return self.leftChild.searchNode(value)

        elif value > self.value and self.rightChild:
            return self.rightChild.searchNode(value)

        return value == self.value

    ## 3 - Deletion

    def deleteNode(self, key, parent):

        if key < self.value and self.leftChild:
            self.leftChild.deleteNode(key, self)
        elif key < self.value:
            return False
        elif key > self.value and self.rightChild:
            self.rightChild.deleteNode(key, self)
        elif key > self.value:
            return False
        else:
            if self.leftChild is None and self.rightChild is None and self == parent.leftChild:
                parent.leftChild = None
                self.clearNode()
            elif self.leftChild is None and self.rightChild is None and self == parent.rightChild:
                parent.rightChild = None
                self.clearNode()

            elif self.leftChile and self.rightChild is None and self == parent.leftChild:
                parent.leftChild = self.leftChild
                self.clearNode()
            elif self.leftChild and self.rightChild is None and self == parent.rightChild:
                parent.rightChild = self.leftChild
                self.clearNode()
            elif self.rightChild and self.leftChild is None and self == parent.leftChild:
                parent.leftChild = self.rightChild
                self.clearNode()
            elif self.rightChild and self.leftChild is None and self == parent.rightChild:
                parent.rightChild = self.rightChild
                self.clearNode()

            else:
                self.value = self.rightChild.findMinValue()
                self.rightChild.removeNode(self.value, self)

    def clearNode(self):
        self.value = None
        self.leftChild = None
        self.rightChild = None

    def findMinVal(self):
        if self.leftChild:
            return self.leftChild.findMinVal()
        else:
            return self.value

    def inOrder(self):

        if self.leftChild:
            self.leftChild.inOrder()

        print(self.value)

        if self.rightChild:
            self.rightChild.inOrder()


bst = BinarySearchTree(15)

bst.insertNode(10)
bst.insertNode(12)
bst.insertNode(20)
bst.insertNode(17)
bst.insertNode(25)
bst.insertNode(19)

print(bst.searchNode(15))
print(bst.searchNode(10))
print(bst.searchNode(17))
print(bst.searchNode(19))
print(bst.searchNode(78))
print(bst.searchNode(20))

bst.inOrder()