class Queue2stack(object):

    def __init__(self):
        self.instack = []
        self.outstack = []

    def enqueue(self,ele):
        return self.instack.append(ele)

    def dequeue(self):
        if len(self.outstack) == 0:
            while(self.instack):
                self.outstack.append(self.instack.pop())

        return self.outstack.pop()

obj = Queue2stack()
obj.enqueue(4)
obj.enqueue(5)
obj.enqueue(6)
obj.enqueue(7)
print(obj.instack)
obj.dequeue()
obj.dequeue()
print(obj.outstack)
