class Node(object):
    def __init__(self, value):
        self.value = value
        self.nextNode = None


class LinkedList(object):
    def __init__(self):
        self.headValue = None

    def printNodeVal(self):
        start = self.headValue

        while start is not None:
            print(start.value)
            start = start.nextNode

    def insertAtBegining(self, newData):
        if self.headValue is None:
            self.headValue = Node(newData)
            return self.headValue

        newNode = Node(newData)
        newNode.nextNode = self.headValue
        self.headValue = newNode
        return self.headValue

    def insertAtMiddle(self, middle_node, newData):
        if middle_node.value is None:
            print("Middle node does not exist")

        newNode = Node(newData)
        newNode.nextNode = middle_node.nextNode
        middle_node.nextNode = newNode

    def insertAtEnd(self, newData):

        if self.headValue is None:
            self.headValue = Node(newData)
            return self.headValue

        start = self.headValue

        while start.nextNode is not None:
            start = start.nextNode
        start.nextNode = Node(newData)


list1 = LinkedList()
T = 11
for val in range(T):
    list1.insertAtBegining(val)

list1.printNodeVal()
print(list1.headValue.value)
