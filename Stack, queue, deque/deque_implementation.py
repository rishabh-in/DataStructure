class Deque(object):
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def pushFront(self,ele):
        return self.items.insert(0, ele)

    def popFront(self):
        return self.items.pop(0)

    def pushLast(self,ele):
        return self.items.append(ele)

    def popLast(self):
        return self.items.pop()

    def size(self):
        return len(self.items)