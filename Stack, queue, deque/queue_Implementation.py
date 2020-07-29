class Queue(object):
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return len(self.items) == 0

    def push(self, ele):
        return self.items.append(ele)

    def pop(self):
        return self.items.pop(0)

    def peek(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)


obj = Queue()
obj.push(4)
obj.push(5)
obj.push(6)
obj.push(7)

print(obj.items)

obj.pop()
print(obj.items)
