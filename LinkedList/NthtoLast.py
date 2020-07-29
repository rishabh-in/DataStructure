class Node(object):
    def __init__(self, value):
        self.value = value
        self.nextNode = None

def nth_to_last(n, head):
    right_point = head
    left_point = head

    for i in range(n-1):
        if not right_point.nextNode:
            raise LookupError("Error: n is larger than the linked list")
        right_point = right_point.nextNode

    while right_point.nextNode:
        left_point = left_point.nextNode
        right_point = right_point.nextNode
    return left_point

a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)
e = Node(5)

a.nextNode = b
b.nextNode = c
c.nextNode = d
d.nextNode = e
result = nth_to_last(3, a)
print(result.value)
