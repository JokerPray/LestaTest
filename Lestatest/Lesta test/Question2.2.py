class CyclicBuffer:
    """
    Реализация циклического буфера FIFO с использованием маски.
    """

    def __init__(self, capacity):

        self.capacity = capacity
        self.mask = (1 << (capacity - 1).bit_length()) - 1
        self.buffer = [None] * self.capacity
        self.head = 0
        self.tail = 0

    def enqueue(self, item):

        if self.is_full():
            raise BufferFullError("Буфер заполнен.")

        self.buffer[self.tail] = item
        self.tail = (self.tail + 1) & self.mask

    def dequeue(self):
        if self.is_empty():
            raise BufferEmptyError("Буфер пуст.")

        item = self.buffer[self.head]
        self.buffer[self.head] = None
        self.head = (self.head + 1) & self.mask
        return item

    def peek(self):
        if self.is_empty():
            raise BufferEmptyError("Буфер пуст.")

        return self.buffer[self.head]

    def is_empty(self):
        return self.head == self.tail

    def is_full(self):
        return (self.tail + 1) & self.mask == self.head

    def __len__(self):
        return (self.tail - self.head) & self.mask

    def __str__(self):
        return str(self.buffer)


class BufferFullError(Exception):
    pass


class BufferEmptyError(Exception):
    pass





