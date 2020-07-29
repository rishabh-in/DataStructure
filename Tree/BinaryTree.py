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

    ############## Traversing algorithm ###################

    ###### DFS #######

    def preOrder(self):
        print(self.value)

        if self.leftChild:
            self.leftChild.preOrder()

        if self.rightChild:
            self.rightChild.preOrder()

    def inOrder(self):

        if self.leftChild:
            self.leftChild.inOrder()

        print(self.value)

        if self.rightChild:
            self.rightChild.inOrder()

    def postOrder(self):

        if self.leftChild:
            self.leftChild.postOrder()

        if self.rightChild:
            self.rightChild.postOrder()

        print(self.value)

    ########## BFS ############
    ## We will use queue data structure to store the

    def BFS(self):

        queue = [self]

        while not len(queue) == 0:
            currentNode = queue.pop(0)
            print(currentNode.value)

            if currentNode.leftChild:
                queue.append(currentNode.leftChild)

            if currentNode.rightChild:
                queue.append(currentNode.rightChild)


root_node = BinaryTree("a")

root_node.insertLeft("b")
root_node.insertRight("c")

node_b = root_node.leftChild
node_b.insertLeft("d")
node_b.insertRight("e")

node_c = root_node.rightChild
node_c.insertLeft("f")
node_c.insertRight("g")

root_node.preOrder()
print("\n")
root_node.inOrder()
print("\n")
root_node.postOrder()
print("\n")
root_node.BFS()