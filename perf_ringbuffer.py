class RingBuffer(object):

    def __init__(self, max_size=10):
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

import time
start_time = time.time()
rb = RingBuffer(1000)
for i in range(50000) :
    rb.enqueue(i)
#    print("Buffer: " + str(rb))
end_time = time.time()
print(f"{end_time - start_time:.5f} sec")
   
