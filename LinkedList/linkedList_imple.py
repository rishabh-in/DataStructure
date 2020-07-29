class Node(object):
    def __init__(self, val):
        self.value = val
        self.nextNode = None

class LinkedList(object):
    def __init__(self):
        self.headValue = None



list1 = LinkedList()
list1.headValue = Node("Mon")
n2 = Node("Tue")
n3 = Node("Wed")

list1.headValue.nextNode = n2
n2.nextNode = n3

print(list1.headValue.value)
print(list1.headValue.nextNode.value)
print(n2.nextNode.value)