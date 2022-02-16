
class Queue:
    # FIFO
    def __init__(self):
        self.list = []
    
    def enqueue(self, value):
        self.list.append(value)
    
    def dequeue(self):
        return self.list.pop(0)


class Stack:
    # LIFO
    def __init__(self):
        self.list = []
    
    def push(self, value):
        self.list.append(value)
    
    def pop(self):
        return self.list.pop(-1)

q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)

s  = Stack()
s.push(1)
s.push(2)
s.push(3)
s.push(4)

for i in range(4):
    print(q.dequeue())

print("**************")

for i in range(4):
    print(s.pop())
