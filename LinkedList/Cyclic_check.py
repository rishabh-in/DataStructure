class Node(object):
    def __init__(self, value):
        self.value = value
        self.nextNode = None


class LinkedList(object):
    def __init__(self):
        self.headValue = None


def cyclic_check(node):
    marker1 = node.headValue
    marker2 = node.headValue

    while marker2 is not None and marker2.nextNode is not None:
        marker1 = marker1.nextNode
        marker2 = marker2.nextNode.nextNode

        if marker1 == marker2:
            return True

    return False


a = LinkedList()
a.headValue = Node(1)
b = Node(2)
c = Node(3)

a.headValue.nextNode = b
b.nextNode = c

print(cyclic_check(a))
