class CircularBuffer(object):

    def __init__(self, max_size=10):
        """Initialize the CircularBuffer with a max_size if set, otherwise"""
        self.buffer = [None] * max_size
        self.head = 0
        self.tail = 0
        self.max_size = max_size

    def __str__(self):
        """Return a formatted string representation of this CircularBuffer."""
        items = ['{!r}'.format(item) for item in self.buffer]
        return '[' + ', '.join(items) + ']'

    def count(self):
        if self.tail >= self.head:
            return self.tail - self.head
        return self.max_size - self.head - self.tail

    def is_empty(self):
        return self.tail == self.head

    def is_full(self):
        return self.tail == (self.head-1) % self.max_size

    def enqueue(self, item):
        if self.is_full():
            raise OverflowError(
                "CircularBuffer is full, unable to enqueue item")
        self.buffer[self.tail] = item
        self.tail = (self.tail + 1) % self.max_size

    def front(self):
        """Return the item at the front of the CircularBuffer
        Runtime: O(1) Space: O(1)"""
        return self.buffer[self.head]

    def dequeue(self):
        if self.is_empty():
            raise IndexError("CircularBuffer is empty, unable to dequeue")
        item = self.buffer[self.head]
        self.buffer[self.head] = None
        self.head = (self.head + 1) % self.max_size
        return item


# Examples
cb = CircularBuffer(8)
print("is Empty: {}".format(cb.is_empty()))
print("is Full: {}".format(cb.is_full()))
print("Buffer: " + str(cb))
print(f"count: {cb.count()}")
print("enqueue 4ea")

cb.enqueue("0")
cb.enqueue("1")
cb.enqueue("2")
cb.enqueue("3")
print("Buffer: " + str(cb))
print(f"count: {cb.count()}")
print("dequeue".format(cb.dequeue()))
print("dequeue".format(cb.dequeue()))
print("Buffer: " + str(cb))
print(f"count: {cb.count()}")
print("enqueue 4ea")
cb.enqueue("4")
cb.enqueue("5")
cb.enqueue("6")
cb.enqueue("7")

print("Buffer: " + str(cb))
print(f"count: {cb.count()}")
print("is Full: {}".format(cb.is_full()))

print("enqueue 1ea")
cb.enqueue("8")
print("is Full: {}".format(cb.is_full()))       # buffer full
print("Buffer: " + str(cb))
print(f"count: {cb.count()}")                   # count 5 ???????????
#print("is Empty: {}".format(cb.is_empty()))
#print("is Full: {}".format(cb.is_full()))
if(cb.is_full()):
    print("dequeue".format(cb.dequeue()))
print("is Full: {}".format(cb.is_full()))
print("Buffer: " + str(cb))
print(f"count: {cb.count()}")                   # count 4 ???????????