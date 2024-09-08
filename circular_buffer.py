class CircularBuffer(object):

    def __init__(self, max_size=10):
        """max_size 미설정 시 default 10"""
        self.buffer = [None] * max_size
        self.front = 0
        self.rear = 0
        self.max_size = max_size

    def __str__(self):
        items = ['{!r}'.format(item) for item in self.buffer]
        return '[' + ', '.join(items) + ']'

    def count(self):
        return ((self.rear - self.front) + self.max_size) % self.max_size

    def is_empty(self):
        return self.rear == self.front

    def is_full(self):
        return self.rear == (self.front-1) % self.max_size

    def enqueue(self, item):
        if self.is_full():
            self.dequeue()
#            raise OverflowError("Buffer is full, unable to enqueue item")
        self.buffer[self.rear] = item
        self.rear = (self.rear + 1) % self.max_size

    def front(self):
        return self.buffer[self.front]

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Buffer is empty, unable to dequeue")
        item = self.buffer[self.front]
        self.buffer[self.front] = None
        self.front = (self.front + 1) % self.max_size
        return item


cb = CircularBuffer(15)
for i in range(0, 20) :
    i += 1
    cb.enqueue(i)
    print("Buffer: " + str(cb))
    print(f"count: {cb.count()}")
    
print("is Empty: {}".format(cb.is_empty()))
print("is Full: {}".format(cb.is_full()))